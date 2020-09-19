# Modelling Salmon Life Cycle in Comox Valley Harbour

## Team members:
- Laura Gutierrez Funderburk (team lead)
- Rachel Dunn (mentor) 
- Anouk de Brouwer
- Courtney Van Den Elzen, University of Colorado Boulder and R Ladies
- B. Eni Owoeye
- Janson Lin, Simon Fraser University
- Pierayeh Vahdani, Simon Fraser University

## Project description

Our goal is to model the life cycle of chinook salmon. We are interested in studying the long term impact of population size of salmon when we introduce microplastic ingestion, as well as fishing and harvesting practices. 
We are also interested in studying the differences in long term chinook salmon population changes resulting from two fishing models: industrial fishing and intertidal modifications (which rely on tide behaviour) used by the Northern Coast Salish Peoples. 


## Datajam Schedule
| Time | Description |
| --- | --- |
| 8:30am | Opening Ceremony |
| 9:30am | Official hack start time! Meet together as team and get to know each other|
| 9:45am | Project brainstorming & defining tasks |
| 10:00am | Optional Git workshop*|
| 10:30am | Hack & work on tasks |
| 12:30pm | Check-in #1: meet back up as a team |
| 1:00pm | Hack & work on tasks |
| 3:30pm | Check-in #2: meet back up as a team |
| | Debugging, prioritizing remaining tasks |
| 5:00pm | Final repository merging |
| | Prepare demo or slides |
| 6:30pm | Project deadline & final Presentation! |
| 7:30pm | Career Panel & Q&A |
| 8:30pm | Awards Ceremony & Closing |


*For those who need help with Git! For those who don't, we can stay on call and continue brainstorming.

## How to use code in this repository

This script contains code that scrapes data from the following website https://www.waterlevels.gc.ca/eng/data for a given location.

We will focus on data from [Comox Valley Harbour](http://comoxharbour.com/location). 

- 2020 Tides https://www.waterlevels.gc.ca/eng/data/table/2020/wlev_sec/7965 
- 2019 Tides https://www.waterlevels.gc.ca/eng/data/table/2019/wlev_sec/7965
- 2018 Tides https://www.waterlevels.gc.ca/eng/data/table/2018/wlev_sec/7965

The python script will take as input:
Website URL
Start date (Year-Month-Day)
End date (Year-Month-Day)
And as output it will return a pandas dataframe (or a CSV) with the data with the following columns:

|Date (YYYY-MM-DD)|Time (24 hour format)|Height-of-tide (meters)|
| - | - | - |


Sample script usage

    python3 scrape_tide_data.py URL start_date end_date
    
## References

1. Krkošek Martin, Hilborn Ray, Peterman Randall M.and Quinn Thomas P.  2011Cycles, stochasticity and density dependence in pink salmon population dynamicsProc. R. Soc. B.2782060–2068 http://doi.org/10.1098/rspb.2010.2335 

2. Desforges JP, Galbraith M, Ross PS. Ingestion of Microplastics by Zooplankton in the Northeast Pacific Ocean. Arch Environ Contam Toxicol. 2015;69(3):320-330. doi:10.1007/s00244-015-0172-5

Data Sources: 
- 2020 Tides https://www.waterlevels.gc.ca/eng/data/table/2020/wlev_sec/7965 
- 2019 Tides https://www.waterlevels.gc.ca/eng/data/table/2019/wlev_sec/7965
- 2018 Tides https://www.waterlevels.gc.ca/eng/data/table/2018/wlev_sec/7965

Ocean Wise The Epic Journey - Follow a Salmon from Egg to Spawner. https://www.youtube.com/watch?v=nkXthUsnRz4&amp;ab_channel=OceanWise 



