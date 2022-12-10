# SolNET
```
Implementation of the paper "SolNet: A Convolutional Neural Network for Detecting Dust on Solar Panels"
Authors:
	Zubayar Mahatab Md Sakif,
	Md. Saif Hassan Onim,
	Adil Ahnaf,
	Ahsan Kabir,
	Rafina Afreen,
	Sumaita Tanjim Hridy,
	Mahtab Hossain,
	Abul Kalam Azad,
	Taskeed Jabid and
	Md Sawkat Ali
```

<p align="center"><img src="data/workflow_all.png" width="90%" alt="" style="background-color:blue"/></p>
<em align="center"> Workflow </em>
<p align="center"><img src="data/solnet_arch.png" width="90%" alt="" style="background-color:white"/></p>
<em align="center"> SolNet Architecture </em>

## Experimental Steps
- Get the dataset from here: [Dataset](https://drive.google.com/drive/folders/12Q3MBI8SPw0vHsO_kkS5izkxw0F7tXx4?usp=sharing)

- Keep the dataset in the dataset folder. You can keep your own dataset for testing purpose.

- Run the 'train.py' from 'utils' folder to train the model

- Run 'evaluate.py' form 'utils' folder to generate loss and acc vs epoch graph.


## Pretrained SolNET
- Get the pretrained SolNet model from here: [Model](https://drive.google.com/drive/folders/1HNJ4fB28DLvzuSoj75qdDAQv9BLeavBs?usp=share_link)

- keep the model in 'models' folder

- Use tensorflows ```predict``` command to test in your own dataset.

## Cite us with the following bibtex:
```
@Article{SolNet2022,
AUTHOR = {Zubayar Mahatab Md Sakif,
	Md. Saif Hassan Onim,
	Adil Ahnaf,
	Ahsan Kabir,
	Rafina Afreen,
	Sumaita Tanjim Hridy,
	Mahtab Hossain,
	Abul Kalam Azad,
	Taskeed Jabid and
	Md Sawkat Ali},
TITLE = {SolNet: A Convolutional Neural Network for Detecting Dust on Solar Panels},
JOURNAL = {Energies},
VOLUME = {HH},
YEAR = {20TT},
NUMBER = {DD},
ARTICLE-NUMBER = {CCCC},
URL = {https://www.mdpi.com/QQQQ},
ISSN = {XXXX-YYYY},
DOI = {AAAA/BBBB}
}
```
