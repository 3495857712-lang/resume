"""
医药知识库检索工具
用于从知识库中检索相关的医药文档、指南和说明书
"""

from langchain.tools import tool
from coze_coding_dev_sdk import KnowledgeClient, Config
from coze_coding_utils.runtime_ctx.context import Context
from coze_coding_utils.log.write_log import request_context
import logging

logger = logging.getLogger(__name__)


@tool
def search_medical_knowledge(query: str, top_k: int = 5) -> str:
    """
    从医药知识库中检索相关的文档和信息。
    
    用于查询药品说明书、临床指南、药监局规定等权威医药资料。
    
    Args:
        query: 检索查询文本，例如"阿司匹林的用法用量"或"高血压用药指南"
        top_k: 返回结果数量，默认5条
        
    Returns:
        检索到的相关文档片段，包含来源和相似度分数
    """
    try:
        # 获取请求上下文
        ctx = request_context.get()
        if ctx is None:
            ctx = Context()
        
        # 初始化知识库客户端
        config = Config()
        client = KnowledgeClient(config=config, ctx=ctx)
        
        # 执行语义搜索
        response = client.search(
            query=query,
            top_k=top_k,
            min_score=0.5  # 设置最小相似度阈值
        )
        
        if response.code != 0:
            logger.error(f"知识库检索失败: {response.msg}")
            return f"知识库检索失败: {response.msg}"
        
        if not response.chunks:
            logger.warning(f"未找到相关内容: {query}")
            return "未在知识库中找到相关内容，请尝试使用不同的关键词查询。"
        
        # 格式化检索结果
        results = []
        for i, chunk in enumerate(response.chunks, 1):
            result_str = f"【文档{i}】相似度: {chunk.score:.2f}\n"
            result_str += f"内容: {chunk.content}\n"
            if chunk.doc_id:
                result_str += f"来源ID: {chunk.doc_id}\n"
            results.append(result_str)
        
        logger.info(f"知识库检索成功，查询: {query}, 返回 {len(response.chunks)} 条结果")
        return "\n".join(results)
        
    except Exception as e:
        error_msg = f"知识库检索异常: {str(e)}"
        logger.error(error_msg, exc_info=True)
        return error_msg
