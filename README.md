# Nasa_Space_apps

# NASA Space Apps Challenge

<img src="https://sa-2019.s3.amazonaws.com/154d29ac/images/covid.png" width="300" height="300"/>
    
# 1. Tracking the VIRUS

The solution makes it possible to solve the pandemic mapping problem. Today, due to the large volume of data to analyze, it ends up being difficult to map each infection point manually. The solution allows to break this barrier, being focused on mapping the contamination on a broader scale. In a real scenario, it is important to detect outbreaks and also possible contaminants, also helping to test individuals. The project uses an algorithm written in python that applies filters to an image to highlight areas of contamination based on prior knowledge of a geographical point of contamination. Through this idea, we use machine learning in order to map areas at risk of contamination for consultation. One way to manage this data should be done in conjunction with society, in which, in Brazil, you can use the data from the SUS card to validate the addresses of patients who have discharged with symptoms of COVID-19 and at the end of the day update the map Of region.

<img src="https://github.com/vitorglemos/Nasa_Space_apps/blob/master/data/intro.png"/>

Project prototype: http://www.trackingthevirus.us/


# 2. Identifying anomalies using Google Trends

Data collected at https://trends.google.com.br/trends/

Here we want to identify whether we can predict any abnormal pattern using Google Trend as a data source to cross-check data on the spread of COVID19. With that, we collected some data using the platform and crossed the main keywords that indicated symptoms related to the disease. To complement this idea, we are also looking for data with the same keywords for 2019, the year the H1N1 epidemic occurred.


This data can be essential to detect some unusual patterns since people use the platform a lot to search for symptoms of some disease. The description of the analysis can be seen below:

## Keywords used and search filters

- **First filter:** (../data/google_trends/filter_1/g1.csv)
    - keyword: [Fever, Dry Cough, Tiredness, Diarrhoea, Headache];
    - Date: 2008-2009 (H1N1);
    - Country: World
- **Second filter:** (../data/google_trends/filter_2/g2.csv)
    - Keyword [Fever, Dry Cough, Tiredness, Diarrhoea, Headache];
    - Date: 2019-2020 (Sars-CoV-2);
    - Contry: World
- **Terceiro filtro:** (../data/google_trends/filter_3/g3.csv)
    - Keyword: [Fever, Dry Cough, Tiredness, Diarrhoea, Headache];
    - Date: 2019-2020 (Sars-CoV-2);
    - Contry: Italy;
   
## Analysis of Graphs for the Prediction Model

The following data are historical searches for symptoms related to viral infections. They all show a higher peak in the event of an infection outbreak. The data generated is based around the world, but this can also be done using place filters on Google Trends. Initially, we can notice 3 things in the following graphics:

#### Filter 1
Some peaks are quite relevant, such as the one that started on 19/04/2009. That same month there were cases related to H1N1.


<img src="https://github.com/vitorglemos/Nasa_Space_apps/blob/master/nasa_proj2/google_predict/data/output_gtrends_f1.png?raw=true">

#### Filter 2

We can note that the search for "Fever" and "Cough" starts on 12/1/2019 and goes up to its maximum on 3/15/2020, which coincides with the cases of Sars-Cov-2.

<img src="https://github.com/vitorglemos/Nasa_Space_apps/blob/master/nasa_proj2/google_predict/data/output_gtrends_f2.png?raw=true">

#### Filter 3
In this case, we separate the case from Italy, here searches also have the same pattern and start to rise in December.


<img src="https://github.com/vitorglemos/Nasa_Space_apps/blob/master/nasa_proj2/google_predict/data/output_gtrends_f3.png?raw=true">


## Predict Models

For prediction, we used the SARIMAX model applied to the data available on [Google Trends](https://trends.google.com.br/) itself:

<img src="https://github.com/vitorglemos/Nasa_Space_apps/blob/master/nasa_proj2/google_predict/data/output_gtrends_f4.png?raw=true"/>

# 3. Using lights to detect more populous and industrialized cities
Satellite images taken from: https://worldwind.arc.nasa.gov/

Here we use satellite data seen at night to compare more populous cities regarding covid infection, some of our comparisons can be seen below:

## REGION 1
<img src="https://github.com/vitorglemos/Nasa_Space_apps/blob/master/nasa_proj2/visual_computing_map/population_industry_detect/data/output_0.jpg"/>

<img src="https://github.com/vitorglemos/Nasa_Space_apps/blob/master/data/covid6.png"/>

## REGION 2
<img src="https://github.com/vitorglemos/Nasa_Space_apps/blob/master/nasa_proj2/visual_computing_map/population_industry_detect/data/output_1.jpg"/>

<img src="https://github.com/vitorglemos/Nasa_Space_apps/blob/master/data/covid2.png"/>

## REGION 3
<img src="https://github.com/vitorglemos/Nasa_Space_apps/blob/master/nasa_proj2/visual_computing_map/population_industry_detect/data/output_2.jpg"/>

<img src="https://github.com/vitorglemos/Nasa_Space_apps/blob/master/data/covid1.png"/>

## REGION 4
<img src="https://github.com/vitorglemos/Nasa_Space_apps/blob/master/nasa_proj2/visual_computing_map/population_industry_detect/data/output_3.jpg"/>

<img src="https://github.com/vitorglemos/Nasa_Space_apps/blob/master/data/covid3.png"/>

## REGION 5
<img src="https://github.com/vitorglemos/Nasa_Space_apps/blob/master/nasa_proj2/visual_computing_map/population_industry_detect/data/output_4.jpg"/>

<img src="https://github.com/vitorglemos/Nasa_Space_apps/blob/master/data/covid4.png"/>


## References:

[NASA DATA](https://worldwind.arc.nasa.gov/)
[PREVISAO DA INFLAÇÃO USANDO SARIMAX](https://analisemacro.com.br/economia/inflacao/previsao-da-inflacao-com-um-modelo-sarimax/)

[STATESPACE SARIMAX STATA](https://www.statsmodels.org/dev/examples/notebooks/generated/statespace_sarimax_stata.html)

