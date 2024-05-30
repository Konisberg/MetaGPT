#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/10 10:30
@Author  : zf
@File    : paper_generation_prompt.py
"""

from enum import Enum

PREFIX = """开始论文写作前，请回答以下问题，以便使用相应的工具："""
FORMAT_INSTRUCTIONS = """请按照下面的格式进行：

问题：你需要回答的问题
思考：你应该如何思考这个问题
行动：采取的行动，应该是以下工具之一 [{tool_names}]
行动输入：行动的输入
观察：行动的结果
...（这个思考/行动/行动输入/观察的过程可以重复N次）
思考：我现在知道最终答案
最终答案：对原始输入问题的最终答案"""
SUFFIX = """让我们开始吧！

问题：{input}
思考：{agent_scratchpad}"""


class PromptString(Enum):
    TOPIC_GENERATION = "以下是一些陈述：\n{memory_descriptions}\n\n基于以上信息，我们能回答关于这些陈述主题的哪3个最突出的高级问题？\n\n{format_instructions}"

    CONTENT_SEARCH = "\n{memory_strings}\n你能从上述陈述中推断出5个高级见解吗？提到人时，请务必指明他们的名字。\n\n{format_instructions}"

    STYLE_ADJUSTMENT = "你是一个文风重要性AI。根据角色的个人资料和记忆描述，评估记忆的重要性，从1到10评分，1表示日常例行（例如，刷牙、铺床），10表示极其深刻（例如，分手、大学录取）。确保你的评分相对于角色的个性和重点。\n\n{format_instructions} 让我们开始！\n\n"

    REVIEW_AND_POLISH = "基于以下记忆，简要总结{full_name}最近的活动。不要编造未明确陈述的细节。对于任何对话，务必提及对话是否已结束或仍在进行中。\n\n{memory_descriptions}"

    EXECUTE_PLAN = "你是一个计划生成AI。你的工作是根据角色的信息（个人资料、目标、最近的活动、当前计划和位置上下文）和他们当前的思考过程，为他们制定新的计划。最终计划应包括至少{time_window}的活动，不超过5个个别计划。按照应执行的顺序列出计划，每个计划详述其描述、地点、开始时间、停止条件和最大持续时间。\n\n{format_instructions}\n\n始终优先完成任何未完成的对话。\n\n让我们开始吧！\n\n"

    OUTPUT_FORMAT = "\n\n(记住！确保你的输出始终遵循以下两种格式之一：\n\nA. 如果你已完成任务：\n思考：'我已完成任务'\n最终回答：<str>\n\nB. 如果你尚未完成任务：\n思考：<str>\n行动：<str>\n行动输入：<str>\n观察：<str>)\n"
