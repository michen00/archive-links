#!/usr/bin/env python3
import markdown
from weasyprint import HTML

# Input and output file paths
input_md = '/tmp/academic_sources/academic_sources_chronological.md'
output_pdf = '/tmp/academic_sources/academic_sources.pdf'

# First create our updated markdown file with chronological ordering
markdown_content = """# Academic Literature on Airport Economics, Marketing and Network Structures

## Table of Contents
1. [Journal Articles](#journal-articles)
2. [Books](#books)

## Journal Articles

### 1. Warnock-Smith, D., Dziedzic, M., & Christidis, P. (2025). Assessing the impact of airport incentive schemes on regional air connectivity differentials across Europe.
*Transport Policy, 162, 106-112.*  
DOI: [10.1016/j.tranpol.2024.11.022](https://doi.org/10.1016/j.tranpol.2024.11.022)

<details>
<summary>Abstract</summary>

This paper presents the results of the widest audit to date of airport incentive schemes across Europe. Using data from 2017 to 2021, incentive schemes for more than 400 airports have been listed and classified by incentive type. The top five categories of incentive were related to new routes, passenger growth, frequency and capacity, confidential agreements and airports with no incentives. The study also detailed change in direct connectivity between 2014 and 2019 for over 1,300 NUTS3 level regions across Europe and for the bottom 40 and top 40 regions by change in direct connectivity. The impact of the absence or presence of airport incentive schemes were assessed using cross-tabulations. The results show that there is limited evidence at a broader level of the employed incentive schemes having an impact on change in direct connectivity over the observed period or indeed on having an impact on the observed air connectivity inequalities that developed across Europe. There is some preliminary evidence that airports that have seen growth in direct connectivity have felt less of a need to offer such a wide range of incentive schemes, providing added weight to the notion that underlying regional economic activity is the key driver for sustainable aviation connectivity growth.
</details>

**Keywords**: Direct air connectivity; Europe; Airport incentive schemes; Airport discounts; Air connectivity disparities

---

### 2. Knorr, A., & Eisenkopf, A. (2025). Slot allocation at capacity-constrained airports: A reform proposal.
*European Transport Studies, 2, 100013.*  
DOI: [10.1016/j.ets.2025.100013](https://doi.org/10.1016/j.ets.2025.100013)

<details>
<summary>Abstract</summary>

Slot allocation at congested airports is based upon administrative procedures in accordance with the guidelines of the International Air Transport Association's (IATA) Worldwide Airports Slot Group. The key principle is the first come, first served rule. As long as airlines do use the slots allotted to them on a regularly basis (the so-called use-it-or-lose-it rule), these will be automatically reallocated to them in the next scheduling period (grandfathering). However, this allocation regime creates a very effective entry barrier for newcomers at slot-constrained airports. Only very few countries, e.g. the UK, permit airlines to trade excess slots on a secondary market. Evidence from these few legal secondary markets – especially at London's Heathrow Airport – clearly demonstrates that the current slot allocation system has produced substantial scarcity rents to the benefit of the incumbent airlines. The existing literature has focused on the potential anticompetitive effects and antitrust implications of grandfathering and on secondary trading of slots only. Our conceptually oriented paper contributes to this literature by adding a property rights perspective to the analysis and by including airports as a new player in the slot allocation game.
</details>

**Keywords**: Slot allocation; IATA Worldwide Scheduling Guidelines; Antitrust; Property rights theory; Airports

---

### 3. Chen, X., Zhang, Z., Xuan, C., & Qiu, R. (2024). Evolutionary analysis of airline networks under different airport-provided subsidy regimes in the context of multiple airport systems.
*Journal of Air Transport Management, 119, 102650.*  
DOI: [10.1016/j.jairtraman.2024.102650](https://doi.org/10.1016/j.jairtraman.2024.102650)

<details>
<summary>Abstract</summary>

To determine the evolutionary trajectory of airline network selection under different airport-provided subsidy regimes in the context of multiple airport systems (MAS), we construct an evolutionary game model consisting of airports and airlines as the two involved parties and explore the evolutionary stable strategies (ESS) of both players under different scenarios, the factors influencing the evolutionary path of the stability strategies are also analyzed. The results show that: (1) ESS of airports is the low subsidy strategy, and airlines may evolve into the hub-spoke network or the point-to-point network. (2) From the perspective of total social welfare, it is preferable for airlines to choose the hub-spoke network. (3) Lower expected subsidies from non-hub airports and higher route fixed costs strongly encourage airlines to converge towards the hub-spoke network strategy as their stable equilibrium. (4) The increase in passenger demand in the MAS can encourage airports to choose the low subsidy strategy, and the increase of passenger demand served by non-hub airports has a dampening effect on the evolution equilibrium toward the hub-spoke network strategy. This study provides valuable insights for improving the airport-provided subsidy schemes and airline network development in MAS.
</details>

**Highlights**:
- An evolutionary game model is developed to analyze airline networks under different airport-provided subsidy regimes in MAS.
- Airports' ESS is low subsidy strategy, airlines may evolve into hub-spoke network or the point-to-point network.
- Lower non-hub subsidies and higher route fixed costs drive airlines towards hub-spoke network strategy.
- Increased passenger demand drives airport and airline convergence toward low subsidy and hub-spoke strategies.

---

### 4. Hou, M., Wang, K., Yang, H., & Zhang, A. (2022). Airport-airline Relationship, Competition and Welfare in a Multi-airport System: The Case of New Beijing Daxing Airport.
*Journal of Transport Economics and Policy, 56(2), 156-189.*  
Link: [Ingenta Connect](https://www.ingentaconnect.com/content/lse/jtep/2022/00000056/00000002/art00003)

<details>
<summary>Abstract</summary>

A game-theoretical model is developed in the context of the regulated multi-airport system (MAS), examining the regulator's policy in airport slot allocation and airlines' airport entry decisions. The regulator has a mixing objective to put different weights on passenger surplus and airports/airlines' profits. It can choose to intervene in airline allocation (that is, one-airport-one-airline rule) or not. It is found when the regulator does not intervene in airline allocation, airlines choose to enter both airports bringing about higher welfare. However, the regulator would intervene if it puts a sufficiently high weight on airports/airlines' profits.
</details>

**Keywords**: Multi-airport systems; airline allocation; airport slots; welfare analysis

---

### 5. Feng, J., Wu, C.-L., & Zhu, J. (2021). Exploring the effect of airport incentive programs: the practice of Narita International Airport.
*Transportation Planning and Technology, 44(7), 785-806.*  
DOI: [10.1080/03081060.2021.1956812](https://doi.org/10.1080/03081060.2021.1956812)

<details>
<summary>Abstract</summary>

Incentive programs are widely used by airports as a marketing tool to attract new services. Empirical evidence regarding the effects of an isolated incentive program is yet to be explored. In this paper, we focus on airports located in Asia to detect the mechanisms, results and effects of the incentive program initiated by Narita International Airport, Japan. We present non-financial and financial indices to explore the effects of incentive schemes. For the non-financial aspect, the retention rate of new air services under incentives is explicitly defined and calculated. Regarding the financial impact, the costs and revenues and tourism revenues of flights under incentive schemes are calculated to estimate the incentive program's financial and economic effects. The results demonstrate that the '2015RDP' incentive program initiated by Narita International Airport has met its strategic goals and achieved success in attracting new services, as well as generating additional revenue for the airport and tourism industry.
</details>

**Keywords**: Airport marketing; incentive scheme; evaluating index; cost–revenue analysis; tourism effects; Narita International Airport

---

## Books

### 1. Florido-Benítez, L. (2024). Airport Marketing Strategies.
*Emerald Publishing Limited.*  
DOI: [10.1108/978-1-83608-082-420241010](https://doi.org/10.1108/978-1-83608-082-420241010)

<details>
<summary>Description</summary>

This book provides an updated global vision of airport marketing strategies in the context of the aviation and tourism sectors. There are many books and articles on marketing and airport marketing, but there is not one yet that speaks directly to airport marketing strategies. This book will substantiate the academic literature regarding the role of airports and their marketing strategies in the aviation and tourism industries. One of the purposes of this book is to understand and document the nature of the airport's management and business through marketing strategies, the distinct challenges that airport and airline operators and Destination Marketing Organizations (DMOs) currently face during these difficult times of economic, social and pandemic periods and how airport operators should try to cope with a global crisis through in coherent, well-planned, coordinated and comprehensive manner.
</details>

---

### 2. Halpern, N., & Graham, A. (2022). Airport Marketing (2nd Edition).
*Routledge, 440 pages.*  
DOI: [10.4324/9781003039563](https://doi.org/10.4324/9781003039563)

<details>
<summary>Description</summary>

This accessible, up-to-date, comprehensive, and in-depth textbook introduces students and practitioners to the principles and practice of airport marketing as well as the major changes and future marketing challenges facing the airport sector. It applies principles of marketing within the airport industry, and examines airport marketing and its environment, how to define and measure the market for airport services, airport strategic marketing planning and individual elements of the airport marketing mix (product, price, distribution and promotion).

The book integrates key elements of marketing theory with airport marketing in practice. Each chapter contains extensive industry examples for different types of airports from around the world to build on the theoretical base of the subject and show real-life applications. This new second edition has been updated to include:

- New and expanded content on branding and the passenger experience, marketing partnerships, engagement marketing and customer relationship management.
- Three brand new chapters on digital marketing, marketing for a more sustainable future, and crisis communications and marketing, in light of the Covid-19 pandemic.
- New, global case studies and examples throughout.

This comprehensive textbook written by two airport marketing experts will be essential reading for air transport students and future managers.
</details>

---
"""

# Write the markdown content to a file
with open(input_md, 'w') as f:
    f.write(markdown_content)

# Now convert to HTML and then PDF
# Read the markdown file
with open(input_md, 'r') as f:
    md_content = f.read()

# Convert markdown to HTML
html = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])

# Create HTML with CSS styling
html_doc = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Academic Literature on Airport Economics</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }}
        h1 {{ color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
        h2 {{ color: #2c3e50; margin-top: 30px; border-bottom: 1px solid #ddd; padding-bottom: 5px; }}
        h3 {{ margin-top: 25px; }}
        details {{ margin-bottom: 15px; padding: 10px; background-color: #f8f9fa; border-radius: 5px; border: 1px solid #ddd; }}
        summary {{ font-weight: bold; cursor: pointer; }}
        hr {{ margin: 30px 0; border: 0; border-top: 1px solid #eee; }}
        a {{ color: #3498db; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    {html}
</body>
</html>"""

# Generate PDF
HTML(string=html_doc).write_pdf(output_pdf)
print(f"PDF successfully created as '{output_pdf}'")
