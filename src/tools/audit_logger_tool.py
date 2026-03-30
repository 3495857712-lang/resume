"""
医药问答审计日志工具
用于记录对话、知识库引用和合规检查结果
"""

from langchain.tools import tool
import logging
import json
import os
from datetime import datetime
from typing import Dict, Any

logger = logging.getLogger(__name__)

# 审计日志文件路径
AUDIT_LOG_DIR = "/app/work/logs/bypass"
AUDIT_LOG_FILE = os.path.join(AUDIT_LOG_DIR, "medical_audit.log")


def _ensure_log_dir():
    """确保日志目录存在"""
    if not os.path.exists(AUDIT_LOG_DIR):
        os.makedirs(AUDIT_LOG_DIR, exist_ok=True)


def _write_audit_log(log_data: Dict[str, Any]):
    """
    写入审计日志
    
    Args:
        log_data: 日志数据字典
    """
    try:
        _ensure_log_dir()
        
        # 添加时间戳
        log_data["timestamp"] = datetime.now().isoformat()
        
        # 写入日志文件
        with open(AUDIT_LOG_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_data, ensure_ascii=False) + "\n")
            
        logger.info(f"审计日志已记录: {log_data.get('event_type', 'unknown')}")
        
    except Exception as e:
        logger.error(f"写入审计日志失败: {str(e)}", exc_info=True)


@tool
def log_conversation(
    user_question: str,
    ai_answer: str,
    knowledge_sources: str = "",
    compliance_result: str = ""
) -> str:
    """
    记录完整的对话交互，包括问题、回答、知识库来源和合规检查结果。
    
    用于审计和追溯医药问答系统的每一次交互。
    
    Args:
        user_question: 用户提出的问题
        ai_answer: AI生成的回答
        knowledge_sources: 知识库检索到的来源文本
        compliance_result: 合规检查结果
        
    Returns:
        日志记录状态
    """
    try:
        log_data = {
            "event_type": "conversation",
            "user_question": user_question,
            "ai_answer": ai_answer,
            "knowledge_sources": knowledge_sources,
            "compliance_result": compliance_result
        }
        
        _write_audit_log(log_data)
        
        return "对话记录已保存到审计日志。"
        
    except Exception as e:
        error_msg = f"记录对话失败: {str(e)}"
        logger.error(error_msg, exc_info=True)
        return error_msg


@tool
def log_knowledge_search(query: str, results: str, doc_count: int = 0) -> str:
    """
    记录知识库检索操作。
    
    Args:
        query: 检索查询
        results: 检索结果
        doc_count: 返回的文档数量
        
    Returns:
        日志记录状态
    """
    try:
        log_data = {
            "event_type": "knowledge_search",
            "query": query,
            "results_summary": results[:500] if len(results) > 500 else results,
            "doc_count": doc_count
        }
        
        _write_audit_log(log_data)
        
        return f"知识库检索记录已保存，查询: {query[:50]}..."
        
    except Exception as e:
        error_msg = f"记录知识库检索失败: {str(e)}"
        logger.error(error_msg, exc_info=True)
        return error_msg


@tool
def log_compliance_check(
    check_type: str,
    content: str,
    result: str,
    violation: bool = False
) -> str:
    """
    记录合规检查操作。
    
    Args:
        check_type: 检查类型 (question/answer)
        content: 被检查的内容
        result: 检查结果
        violation: 是否违规
        
    Returns:
        日志记录状态
    """
    try:
        log_data = {
            "event_type": "compliance_check",
            "check_type": check_type,
            "content_summary": content[:200] if len(content) > 200 else content,
            "result": result,
            "violation": violation
        }
        
        _write_audit_log(log_data)
        
        status = "违规" if violation else "合规"
        return f"合规检查记录已保存，状态: {status}"
        
    except Exception as e:
        error_msg = f"记录合规检查失败: {str(e)}"
        logger.error(error_msg, exc_info=True)
        return error_msg
