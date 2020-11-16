case_data = read.table("BCCDC_COVID19_Dashboard_Case_Details.csv", sep = ",", header = TRUE)

#Filter the case data in October, name the subset "oct_case"
case_data$Reported_Date = as.Date(case_data$Reported_Date, format="%Y-%m-%d")
oct_case =subset(case_data, Reported_Date >= "2020-10-01" & Reported_Date <= "2020-10-31")

#Process oct data by tabulating the data for everyday in Oct
oct_case$Reported_Date = as.Date(oct_case$Reported_Date, format="%Y-%m-%d")
tab = table(cut(oct_case$Reported_Date, 'day'))

#Get the case number (frequency) for everyday in Oct
frequencies = data.frame(Date=format(as.Date(names(tab)), '%Y-%m-%d'), Frequency=as.vector(tab))

#Plot the number of cases vs day in Oct
library(ggplot2)
ggplot(frequencies, aes(x=Date, group=1))+
  geom_line(aes(y=Frequency))+
  labs(title="October Covid-19 cases vs Day", y="Number of Cases")
