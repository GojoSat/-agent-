import os
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

class Agent:
    def __init__(self, role, system_prompt):
        self.role = role
        self.system_prompt = system_prompt

    def run(self, input_text):
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": input_text}
            ]
        )
        return response.choices[0].message.content

research_agent = Agent("Researcher", "你是一个专业市场研究员，负责收集信息并总结关键要点")
writer_agent = Agent("Writer", "你是一个内容创作者，根据提供的信息写一篇结构清晰的文章")
optimizer_agent = Agent("Optimizer", "你是一个内容优化专家，负责提升文章质量，让表达更流畅、更吸引人")

class TaskManager:
    def execute(self, topic):
        print(f"任务开始: {topic}")
        research = research_agent.run(f"请调研：{topic}")
        article = writer_agent.run(f"根据以下信息写文章：\n{research}")
        final = optimizer_agent.run(f"优化这篇文章：\n{article}")
        return final

if __name__ == "__main__":
    manager = TaskManager()
    topic = input("请输入主题: ")
    result = manager.execute(topic)
    print(result)
