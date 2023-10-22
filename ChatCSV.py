#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip -q install langchain openai')
import os

os.environ["OPENAI_API_KEY"] = "" #Add API Code
get_ipython().system('pip show langchain')
import pandas as pd
df=pd.read_csv('C:/Users/Admin/Downloads/archive (2)/train.csv')
df.head()
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
agent=create_csv_agent(OpenAI(temperature=0),'C:/Users/Admin/Downloads/archive (2)/train.csv',verbose=True)
agent
agent.agent.llm_chain.prompt.template


agent.run("how many rows are there")
agent.run("How many are males")
agent.run("how many people have stayes more than 3 years in the city and are females")

