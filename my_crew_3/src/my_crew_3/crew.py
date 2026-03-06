from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import os

os.environ["GROQ_API_KEY"] = "x"

llm = LLM(
    model="groq/llama-3.1-8b-instant",
    temperature=0
)

@CrewBase
class AnalyticalCrew():

    agents: List[BaseAgent]
    tasks: List[Task]

    # -------- AGENTS -------- #

    @agent
    def input_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['input_agent'],
            llm=llm,
            verbose=True
        )

    @agent
    def keyword_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['keyword_agent'],
            llm=llm,
            verbose=True
        )

    @agent
    def story_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['story_agent'],
            llm=llm,
            verbose=True
        )

    @agent
    def evaluation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['evaluation_agent'],
            llm=llm,
            verbose=True
        )

    @agent
    def report_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['report_agent'],
            llm=llm,
            verbose=True
        )

    # -------- TASKS -------- #

    @task
    def input_task(self) -> Task:
        return Task(
            config=self.tasks_config['input_task']
        )

    @task
    def keyword_task(self) -> Task:
        return Task(
            config=self.tasks_config['keyword_task']
        )

    @task
    def story_task(self) -> Task:
        return Task(
            config=self.tasks_config['story_task']
        )

    @task
    def evaluation_task(self) -> Task:
        return Task(
            config=self.tasks_config['evaluation_task']
        )

    @task
    def report_task(self) -> Task:
        return Task(
            config=self.tasks_config['report_task'],
            output_file="final_report.md"
        )

    # -------- CREW -------- #

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )