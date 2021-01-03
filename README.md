<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/brenoslivio/SCC0652_Computational_Visualization/">
    <img src="https://raw.githubusercontent.com/brenoslivio/SCC0652_Computational_Visualization/master/index.png" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center">Computational Visualization</h3>

  <p align="center">
    Projects for the course SCC0652 Computational Visualization using concepts like data processing, data visualization and interactive visualization.
    <br />
    <br />
    <strong> Authors: </strong> Afonso Henrique, <a href="https://github.com/Afonso-H-P-Garcia"> Afonso-H-P-Garcia </a>
    <br />
    Breno Lívio, <a href="https://github.com/brenoslivio/"> brenoslivio </a>
    <br />
    Vitor Gratiere Torres, <a href="https://github.com/vitorgt"> vitorgt </a>
    <br />
    <br />
    <a href="https://github.com/brenoslivio/SCC0652_Computational_Visualization/"><strong>Explore the docs »</strong></a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->

<summary><h2 style="display: inline-block">Table of Contents</h2></summary>
<ol>
  <li>
    <a href="#about-the-project">About The Project</a>
  </li>
  <li>
    <a href="#getting-started">Getting Started</a>
    <ul>
      <li><a href="#prerequisites">Prerequisites</a></li>
      <li><a href="#installation">Installation</a></li>
    </ul>
  </li>
  <li><a href="#license">License</a></li>
  <li><a href="#acknowledgements">Acknowledgements</a></li>
</ol>


<!-- ABOUT THE PROJECT -->
## About The Project

The projects are intended for the course SCC0652 - Computational Visualization, at ICMC - USP, 2nd semester of 2020. The subjects treated were:

'Introduction: scientific, information, and software visualization. Problems and limitations of visualization. Using the computer to data analysis. Basic techniques of visualization: techniques classification and data. Organization and data types in visualization. Volume visualization techniques. Surface-based volume visualization techniques. Direct volume rendering techniques. Comparison between direct volume rendering and surface-based techniques. Vector visualization. Multidimensional data visualization: registers, text, temporal series, images and other. Attribute and instance based mapping techniques. Dimensionality reduction and its application on visualization. Associations and examples of visualization with data mining (visual data mining). Graph and tree based visualization. Visualization systems. Introduction to a visualization system. Examples and practice.'

For more information about the course check [here](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=SCC0652&codcur=97001&codhab=0).

Considering the course subject, we chose a Pokémon dataset to use the proper visualization techniques.

The projects are Jupyter Notebooks divided in three subjects studied throughout the course:

### [Data processing](https://nbviewer.jupyter.org/github/brenoslivio/SCC0652_Computational_Visualization/blob/master/notebooks/Project-1/Projeto_1_Processamento_de_dados.ipynb)

Choosing the Pokémon dataset, we had to process the data, cleaning, adding relevant information for the dataset. We joined a dataset from [Kaggle](https://www.kaggle.com/mariotormo/complete-pokemon-dataset-updated-090420) with data scrapped from [Pokémon Database](https://pokemondb.net/pokedex/all).

### [Data visualization](https://nbviewer.jupyter.org/github/brenoslivio/SCC0652_Computational_Visualization/blob/master/notebooks/Project-2/Projeto_2_Visualizacao_de_dados.ipynb)

With the data processed, we made all the different kind of visualizations with the intent of understanding the dataset even more. Notable visualizations made were Boxplot, Violin Plot, correlation heatmap for Pearson and Spearman, Scatter plot, Pairplot and Word cloud.

### [Interactive visualization](https://nbviewer.jupyter.org/github/brenoslivio/SCC0652_Computational_Visualization/blob/master/notebooks/Project-3/Projeto_3_Visualizacao_interativa.ipynb) 

Finally, the last project make the visualization interactive, allowing the user explore the dataset with proper input from the keyboard and mouse. Graphs like boxplot, violin plot, scatter plot. Beyond that, we created a functional Pokédex with ipywidgets. (Important: Widgets aren't rendered properly with nbviewer).

You can check the complete documentation (Brazilian Portuguese) for the projects [here](https://github.com/brenoslivio/SCC0652_Computational_Visualization/blob/master/SCC0652___Projeto_Pok_mon.pdf).

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Python 3.8 or greater, Jupyter Notebook. There are some libraries you may need to install for importing like ipywidgets, matplotlib and etc.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/brenoslivio/SCC0652_Computational_Visualization.git
   ```
2. Simply run Jupyter Notebook to open the projects.

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [JúpiterWeb](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=SCC0652&codcur=97001&codhab=0)
* [Complete Pokemon Dataset, Mario Tormo Romero](https://www.kaggle.com/mariotormo/complete-pokemon-dataset-updated-090420)
* [Pokémon Database](https://pokemondb.net/pokedex/all)
