*Code and data for the exploring the possible relationship between tech layoffs and production in AI.*

# Layoffs and AI: Uncovering the Hidden Relationship
Are recent layoffs from Meta and other tech companies adversely affecting the production of artificial intelligence research?

# Introduction
The tech industry has seen an upwards trend of layoffs in recent years, with many companies downsizing their workforce or cutting jobs to stay both competitive and reduce costs. At the same time, the production of advanced artificial intelligence (AI) models has also been on the rise, seeing many tech companies heavily investing in AI research and development [[1](#Sources)].

In this blog post, I will explore the possible relationship between the layoffs in tech and the production of AI models as well as attempt to understand the factors that may be driving this relationship.

# Results & Discussion
To investigate the relationship between tech layoffs and AI production, I collected data from Crunchbase's dataset from [[2](#Sources)]. According to Figure 1, the number of tech layoffs has been trending slightly upward in 2022. This is significant because it suggests that companies are cutting their human workforce in favor of investing more in AI technology. Because of the nature of this exploration, the data only shows the trend of tech layoffs and not the reasons behind them. Additional data and analysis would be needed to support this claim. Further exploration would take data from a variety of sources, including reports and statistics from studies on the state of the AI industry, and data on the number of job openings and job postings in the tech industry. It's possible that factors such as market conditions or changes in consumer demand may affect both tech layoffs and AI production.

![[layoffs_by_date.png]]
**Figure 1** *illustrates the number of layoffs in 2022 for 232 tech companies[[2](#Sources)]. The rolling average is taken as the average of the number of layoffs over a four-month period. The table at the end of the page shows relevant statistics.*

One major factor that may be contributing to this trend is the increasing use of automation and AI in the tech industry. Many companies are replacing human workers with AI systems that can perform tasks more quickly and efficiently as we have seen during the COVID-19 Pandemic [[5](#Sources)]. This may lead to job losses in areas such as customer service, data analysis, and - with the introduction of Github's Autopilot - software development. Furthermore, an investigation, such as [1][(#Sources)], looking at the companies that are investing heavily into AI research and development may yield a trend that correlates with Figure 1. Figure 2 shows release months for models created this year by teams of laid-off developers or academic institution, out of OpenAI's GPT-3 large language model[[3](#Sources)]. 

![[Picture1.png]]
**Figure 2** *shows *

## Statistics
```` 
Max: 11,000 (Layoffs)
Min: 5
Mean: 367
Median: 90
Std: 1150
```` 
# Methods & Reproducibility
Layoff data was sourced from [[2](#Sources)]. The data was formatted into a csv file and loaded into a Pandas Dataframe [[4](#Sources)]. Further processing of the data included removing  "nan" values and "Unclear" values from the Number of Layoffs column. The Github repository for this project can be found at: https://github.com/nissmogt/trendsAI/tree/main.


# Concluding Remarks
This article explores the possible relationship between current layoffs in tech and AI production. Additionally, this article presents data on the slight increase in the number of tech layoffs in 2022 and suggests a possible relationship between these layoffs and an increase in AI production. However, additional data and analysis would be needed to fully understand the relationship between the two and to support the claim that companies are cutting their human workforce in favor of investing in AI technology.

# Sources
[1] What’s New in Artificial Intelligence from the 2022 Gartner Hype Cycle https://www.gartner.com/en/articles/what-s-new-in-artificial-intelligence-from-the-2022-gartner-hype-cycle
[2] Tech Layoffs In 2022: The U.S. Companies That Have Cut Jobs https://news.crunchbase.com/startups/tech-layoffs-2022/
[3] State of AI 2022 Report https://www.stateof.ai/
[4] Pandas Python Library https://pandas.pydata.org
[5] Millions of Americans Have Lost Jobs in the Pandemic—And Robots and AI Are Replacing Them Faster Than Ever https://time.com/5876604/machines-jobs-coronavirus/
