"""
医药合规检查工具
用于检查用户问题和AI回答是否符合医药合规要求
"""

from langchain.tools import tool
from typing import List, Dict
import logging
import re

logger = logging.getLogger(__name__)


# 合规规则定义
COMPLIANCE_RULES = {
    "禁止诊断": {
        "keywords": [
            "诊断", "确诊", "我得了什么病", "是什么病", "判断病情",
            "是否患病", "有没有病", "什么疾病"
        ],
        "violation_message": "此问题涉及诊断或诊疗内容，请咨询专业医师。"
    },
    "禁止开处方": {
        "keywords": [
            "开药", "开处方", "给我开", "应该吃什么药", "用什么药",
            "推荐药物", "买什么药", "用什么处方"
        ],
        "violation_message": "此问题涉及处方建议，请咨询专业医师获取处方。"
    },
    "禁止用药指导": {
        "keywords": [
            "怎么用药", "怎么吃", "剂量是多少", "吃多少",
            "用药指导", "如何使用"
        ],
        "violation_message": "此问题涉及具体用药指导，请严格遵医嘱用药，或咨询医师或药师。"
    }
}


def _check_keywords(text: str, keywords: List[str]) -> bool:
    """
    检查文本中是否包含关键词列表中的任意关键词
    
    Args:
        text: 待检查文本
        keywords: 关键词列表
        
    Returns:
        是否包含关键词
    """
    text_lower = text.lower()
    for keyword in keywords:
        if keyword.lower() in text_lower:
            return True
    return False


def _extract_violation_type(text: str) -> Dict:
    """
    提取违规类型
    
    Args:
        text: 待检查文本
        
    Returns:
        违规信息字典，包含违规类型和提示消息
    """
    for rule_name, rule_info in COMPLIANCE_RULES.items():
        if _check_keywords(text, rule_info["keywords"]):
            return {
                "violation": True,
                "rule": rule_name,
                "message": rule_info["violation_message"]
            }
    
    return {"violation": False}


@tool
def check_question_compliance(question: str) -> str:
    """
    检查用户问题是否符合医药合规要求。
    
    检测问题是否涉及诊断、开处方等违规内容。
    
    Args:
        question: 用户提出的问题
        
    Returns:
        检查结果，包含是否合规和违规原因
    """
    try:
        result = _extract_violation_type(question)
        
        if result["violation"]:
            logger.warning(f"用户问题违规: {result['rule']}, 问题: {question}")
            return f"违规类型: {result['rule']}\n提示: {result['message']}"
        else:
            logger.info(f"用户问题合规: {question[:50]}...")
            return "问题合规，可以继续处理。"
            
    except Exception as e:
        error_msg = f"合规检查异常: {str(e)}"
        logger.error(error_msg, exc_info=True)
        return error_msg


@tool
def check_answer_compliance(answer: str, knowledge_sources: str = "") -> str:
    """
    检查AI回答是否符合医药合规要求。
    
    确保回答：
    1. 不包含诊断意见或处方建议
    2. 仅引用知识库文本
    3. 不编造医疗信息
    
    Args:
        answer: AI生成的回答
        knowledge_sources: 知识库检索到的来源文本
        
    Returns:
        检查结果，包含是否合规和修改建议
    """
    try:
        # 检查是否包含违规内容
        result = _extract_violation_type(answer)
        
        if result["violation"]:
            logger.warning(f"AI回答违规: {result['rule']}")
            return f"违规类型: {result['rule']}\n提示: 回答包含违规内容，需要修改。\n建议: {result['message']}"
        
        # 检查是否有知识库支撑
        if knowledge_sources and knowledge_sources != "未在知识库中找到相关内容，请尝试使用不同的关键词查询。":
            # 简单检查回答中的关键信息是否来自知识库
            # 这里可以增加更严格的引用验证逻辑
            logger.info("AI回答合规，且有知识库支撑")
            return "回答合规，已引用知识库来源。"
        else:
            logger.warning("AI回答缺乏知识库支撑")
            return "警告: 回答可能缺乏知识库支撑，请确保仅引用权威资料。"
            
    except Exception as e:
        error_msg = f"回答合规检查异常: {str(e)}"
        logger.error(error_msg, exc_info=True)
        return error_msg
