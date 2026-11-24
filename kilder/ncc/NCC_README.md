---
YAML tags: null
annotations_creators:
- no-annotation
language_creators:
- found
language:
- en
- nb
- 'no'
- nn
- sv
- da
- is
- fo
license: cc
multilinguality:
- multilingual
pretty_name: NCC
size_categories:
- 2G<n<1B
source_datasets:
- original
task_categories:
- text-generation
task_ids:
- language-modeling

---
# Dataset Card for NbAiLab/NCC


## Table of Contents
- [Dataset Description](#dataset-description)
- [Dataset Summary](#dataset-summary)
- [Data Fields](#data-fiels)
- [Dataset Creation](#dataset-creation)
- [Statistics](#statistics)
- [Document Types](#document-types)
- [Languages](#languages)
- [Publish Periode](#publish-periode)
- [Considerations for Using the Data](#considerations-for-using-the-data)
- [Social Impact of Dataset](#social-impact-of-dataset)
- [Discussion of Biases](#discussion-of-biases)
- [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
- [Dataset Curators](#dataset-curators)
- [Licensing Information](#licensing-information)
- [Citation Information](#citation-information)

## Dataset Description
- **Homepage:** https://github.com/NbAiLab/notram
- **Repository:** https://github.com/NbAiLab/notram
- **Paper:** https://arxiv.org/abs/2104.09617
- **Point of Contact:** [Freddy Wetjen](mailto:freddy.wetjen@nb.no)


---
<div style="border: 2px solid red; padding: 10px; border-radius: 5px;">

### ⚠️ Important Update (December 2024)

Previously, newspapers were a significant part of the Norwegian Colossal Corpus (NCC), particularly the newspapers distributed under the so called "Språkbank-avtalen". As of December 2024, at the request of media houses, we have ceased distributing newspapers under this agreement, including the "Norsk Aviskorpus." However, NCC still includes numerous newspapers that are released under more open agreements.

</div>

---

The Norwegian Colossal Corpus is a collection of multiple smaller Norwegian corpuses suitable for training large language models. We have done extensive cleaning on the datasets, and have made them available in a common format. The total size of the NCC is currently 30GB. The cleaning of the dataset is optimised for encoder models. If you are building a decoder model, it is usually advised to be a bit stricter on the cleaning procedure. We have included meta-data like source, publication year and languaguage confidence to aid this cleaning.


## Licenses
| Corpus                 | License                                                                          |
|------------------------|----------------------------------------------------------------------------------|
| Library Newspapers     | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)                    |
| Library Books          | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)                    |
| LovData CD             | [NLOD 2.0](https://data.norge.no/nlod/en/2.0/)                                    |
| Government Reports     | [NLOD 2.0](https://data.norge.no/nlod/en/2.0/)                                    |
| Parliament Collections | [NLOD 2.0](https://data.norge.no/nlod/en/2.0/)                                    |
| Public Reports         | [NLOD 2.0](https://data.norge.no/nlod/en/2.0/)                                    |
| Målfrid Collection     | [NLOD 2.0](https://data.norge.no/nlod/en/2.0/)                                    |
| Wikipedia              | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)                  |


## How to Use
```python
from datasets import load_dataset
data = load_dataset("NbAiLab/NCC", streaming=True)
```
## Download Data
If you do not want to use the HuggingFace Dataset-library for training, or if you want to do additional pre-processing, it is also possible to download the files locally.
```bash
# Clone the training set
git clone https://huggingface.co/datasets/NbAiLab/NCC

# Create one large training file of all shards without unpacking
cat NCC/data/train*.gz > onefile.json.gz
```

<details>
<summary>List of all the files.</summary>


* [train-shard-0001-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0001-of-0046.json.gz)
* [train-shard-0002-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0002-of-0046.json.gz)
* [train-shard-0003-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0003-of-0046.json.gz)
* [train-shard-0004-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0004-of-0046.json.gz)
* [train-shard-0005-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0005-of-0046.json.gz)
* [train-shard-0006-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0006-of-0046.json.gz)
* [train-shard-0007-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0007-of-0046.json.gz)
* [train-shard-0008-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0008-of-0046.json.gz)
* [train-shard-0009-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0009-of-0046.json.gz)
* [train-shard-0010-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0010-of-0046.json.gz)
* [train-shard-0011-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0011-of-0046.json.gz)
* [train-shard-0012-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0012-of-0046.json.gz)
* [train-shard-0013-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0013-of-0046.json.gz)
* [train-shard-0014-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0014-of-0046.json.gz)
* [train-shard-0015-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0015-of-0046.json.gz)
* [train-shard-0016-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0016-of-0046.json.gz)
* [train-shard-0017-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0017-of-0046.json.gz)
* [train-shard-0018-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0018-of-0046.json.gz)
* [train-shard-0019-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0019-of-0046.json.gz)
* [train-shard-0020-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0020-of-0046.json.gz)
* [train-shard-0021-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0021-of-0046.json.gz)
* [train-shard-0022-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0022-of-0046.json.gz)
* [train-shard-0023-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0023-of-0046.json.gz)
* [train-shard-0024-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0024-of-0046.json.gz)
* [train-shard-0025-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0025-of-0046.json.gz)
* [train-shard-0026-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0026-of-0046.json.gz)
* [train-shard-0027-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0027-of-0046.json.gz)
* [train-shard-0028-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0028-of-0046.json.gz)
* [train-shard-0029-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0029-of-0046.json.gz)
* [train-shard-0030-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0030-of-0046.json.gz)
* [train-shard-0031-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0031-of-0046.json.gz)
* [train-shard-0032-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0032-of-0046.json.gz)
* [train-shard-0033-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0033-of-0046.json.gz)
* [train-shard-0034-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0034-of-0046.json.gz)
* [train-shard-0035-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0035-of-0046.json.gz)
* [train-shard-0036-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0036-of-0046.json.gz)
* [train-shard-0037-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0037-of-0046.json.gz)
* [train-shard-0038-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0038-of-0046.json.gz)
* [train-shard-0039-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0039-of-0046.json.gz)
* [train-shard-0040-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0040-of-0046.json.gz)
* [train-shard-0041-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0041-of-0046.json.gz)
* [train-shard-0042-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0042-of-0046.json.gz)
* [train-shard-0043-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0043-of-0046.json.gz)
* [train-shard-0044-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0044-of-0046.json.gz)
* [train-shard-0045-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0045-of-0046.json.gz)
* [train-shard-0046-of-0046](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/train-shard-0046-of-0046.json.gz)
* [validation-shard-0001-of-0001](https://huggingface.co/datasets/NbAiLab/NCC/resolve/main/data/validation-shard-0001-of-0001.json.gz)


</details>

### Dataset Summary
The NCC dataset contains json lines with language training data. Here is an example json line:
```json
{
"id": "1006205",
"doc_type": "cc100",
"publish_year": 2021,
"lang_fasttext": "nn",
"lang_fasttext_conf": "0.641",
"text": "Eg har ein PLAN! KOS deg og ha ei fin helg"
}
```
## Data Fields
|**id:** | String with id to source of line and a unique identifier|
|:-----------|:------------|
|**doc_type** | String describing type of media text extracted from (I.e. book,newspaper etc)|
|**publish_year** | Integer. The year text published. When year is undetermined it is set to 2021.|
|**lang_fasttext** | String. Language of text identified by FastText|
|**lang_fasttext_conf** | String. Confidence calculated by FastText|
|**text** | String. The complete utf-8 document. If longer than 1M characters it is split.|

### Dataset Creation
We are providing a **train** and a **validation** split. The standard size of the validation is a single 650Mb file, while train is sharded in 650Mb chunks.


Build date original corpus: 21012022
Build data revised corpus: 10032025


#### Initial Data Collection and Curation
The procedure for the dataset creation is described in detail in our papers.

### Summary
| Words         | Documents   |   Words/Document |
|--------------:|------------:|-----------------:|
| 4,629,683,886 | 8,176,399   |              566 |

### Document Types
| Source                                | Words         | Documents   | Words/Document   |
|--------------------------------------:|--------------:|------------:|-----------------:|
| parliament                            | 1,301,766,124 | 9,528       | 136,625          |
| books                                 | 861,465,925   | 24,253      | 35,519           |
| maalfrid_regjeringen                  | 368,581,048   | 940,936     | 391              |
| maalfrid_ssb                          | 286,024,843   | 871,262     | 328              |
| maalfrid_uio                          | 186,003,662   | 788,988     | 235              |
| government_nb                         | 136,708,062   | 3,557       | 38,433           |
| newspaper_ocr                         | 129,670,570   | 665,344     | 194              |
| wikipedia_download_nbo                | 113,329,164   | 535,461     | 211              |
| maalfrid_fylkesmannen                 | 105,197,012   | 473,582     | 222              |
| publicreports                         | 80,064,396    | 3,365       | 23,793           |
| maalfrid_nve                          | 68,194,532    | 308,924     | 220              |
| maalfrid_patentstyret                 | 66,482,941    | 218,930     | 303              |
| maalfrid_ntnu                         | 59,108,734    | 203,770     | 290              |
| lovdata_cd_odelsting_2005             | 37,295,277    | 1,987       | 18,769           |
| maalfrid_vegvesen                     | 34,177,216    | 169,998     | 201              |
| maalfrid_fhi                          | 33,541,094    | 147,668     | 227              |
| maalfrid_norad                        | 33,454,343    | 95,191      | 351              |
| maalfrid_skatteetaten                 | 33,313,015    | 84,448      | 394              |
| maalfrid_uib                          | 29,049,822    | 118,328     | 245              |
| wikipedia_download_nno                | 27,663,552    | 146,512     | 188              |
| maalfrid_forskningsradet              | 24,647,599    | 75,104      | 328              |
| maalfrid_nasjonalparkstyre            | 21,795,981    | 95,990      | 227              |
| government_nn                         | 18,610,692    | 1,091       | 17,058           |
| maalfrid_nmbu                         | 18,493,389    | 71,320      | 259              |
| maalfrid_oslomet                      | 18,140,360    | 48,140      | 376              |
| maalfrid_domstol                      | 17,073,430    | 52,233      | 326              |
| maalfrid_banenor                      | 16,805,767    | 71,933      | 233              |
| maalfrid_nav                          | 16,651,084    | 75,792      | 219              |
| maalfrid_landbruksdirektoratet        | 13,398,273    | 49,021      | 273              |
| maalfrid_helsedirektoratet            | 13,312,827    | 50,476      | 263              |
| maalfrid_nokut                        | 10,332,870    | 39,426      | 262              |
| maalfrid_hi                           | 10,272,572    | 39,923      | 257              |
| maalfrid_norges-bank                  | 10,135,291    | 37,988      | 266              |
| maalfrid_udir                         | 10,102,549    | 39,632      | 254              |
| maalfrid_vkm                          | 10,041,892    | 32,960      | 304              |
| maalfrid_nbim                         | 9,841,446     | 18,532      | 531              |
| maalfrid_miljodirektoratet            | 9,704,590     | 35,482      | 273              |
| maalfrid_distriktssenteret            | 9,598,023     | 39,415      | 243              |
| maalfrid_ngu                          | 9,454,229     | 35,414      | 266              |
| maalfrid_ptil                         | 9,416,592     | 35,024      | 268              |
| maalfrid_nord                         | 9,192,052     | 45,786      | 200              |
| maalfrid_fiskeridir                   | 8,482,774     | 34,167      | 248              |
| maalfrid_hivolda                      | 7,993,548     | 27,057      | 295              |
| maalfrid_difi                         | 7,971,205     | 36,605      | 217              |
| maalfrid_mattilsynet                  | 7,663,012     | 27,614      | 277              |
| maalfrid_havarikommisjonen            | 7,607,533     | 25,552      | 297              |
| maalfrid_kulturradet                  | 7,364,355     | 22,951      | 320              |
| maalfrid_ks                           | 7,065,314     | 28,029      | 252              |
| maalfrid_kystverket                   | 6,870,772     | 31,694      | 216              |
| maalfrid_udi                          | 6,566,701     | 19,529      | 336              |
| maalfrid_uia                          | 6,094,660     | 24,397      | 249              |
| maalfrid_hjelpemiddeldatabasen        | 6,029,923     | 34,946      | 172              |
| maalfrid_khrono                       | 5,993,140     | 20,431      | 293              |
| maalfrid_helsetilsynet                | 5,913,602     | 18,721      | 315              |
| maalfrid_moreforsk                    | 5,755,447     | 22,089      | 260              |
| maalfrid_jernbanedirektoratet         | 5,589,074     | 22,150      | 252              |
| maalfrid_veiviseren                   | 5,438,472     | 18,441      | 294              |
| lovdata_cd_somb_rundskriv_2005        | 5,400,486     | 3,284       | 1,644            |
| maalfrid_dsb                          | 5,312,625     | 18,200      | 291              |
| lovdata_cd_sentrale_forskrifter_2005  | 5,178,059     | 11,745      | 440              |
| maalfrid_husbanken                    | 4,810,203     | 15,375      | 312              |
| maalfrid_legemiddelverket             | 4,795,154     | 20,634      | 232              |
| maalfrid_vetinst                      | 4,776,782     | 14,839      | 321              |
| maalfrid_imdi                         | 4,744,408     | 15,642      | 303              |
| maalfrid_forsvarsbygg                 | 4,672,409     | 19,287      | 242              |
| maalfrid_sdir                         | 4,640,185     | 15,547      | 298              |
| maalfrid_konkurransetilsynet          | 4,618,590     | 12,912      | 357              |
| maalfrid_arkivverket                  | 4,603,524     | 16,899      | 272              |
| maalfrid_dsa                          | 4,595,530     | 16,242      | 282              |
| maalfrid_hiof                         | 4,580,991     | 23,675      | 193              |
| maalfrid_ehelse                       | 4,478,908     | 23,074      | 194              |
| maalfrid_inn                          | 4,420,070     | 26,840      | 164              |
| maalfrid_klagenemndssekretariatet     | 4,287,067     | 12,208      | 351              |
| maalfrid_sprakradet                   | 4,180,404     | 15,521      | 269              |
| maalfrid_nhh                          | 4,063,920     | 16,068      | 252              |
| maalfrid_dibk                         | 4,058,208     | 15,855      | 255              |
| maalfrid_kartverket                   | 3,814,376     | 19,110      | 199              |
| maalfrid_riksrevisjonen               | 3,783,728     | 11,216      | 337              |
| maalfrid_toll                         | 3,595,842     | 14,122      | 254              |
| maalfrid_nibio                        | 3,531,231     | 17,464      | 202              |
| maalfrid_met                          | 3,528,846     | 18,689      | 188              |
| maalfrid_bufdir                       | 3,425,362     | 11,720      | 292              |
| maalfrid_artsdatabanken               | 3,275,378     | 9,242       | 354              |
| maalfrid_politiet                     | 3,239,913     | 10,728      | 302              |
| maalfrid_nkom                         | 3,197,196     | 10,214      | 313              |
| maalfrid_vestlandfylke                | 3,127,665     | 12,337      | 253              |
| maalfrid_uis                          | 2,988,424     | 10,045      | 297              |
| maalfrid_sykkelbynettverket           | 2,880,916     | 12,086      | 238              |
| maalfrid_nlr                          | 2,702,753     | 16,178      | 167              |
| maalfrid_seniorporten                 | 2,672,667     | 8,295       | 322              |
| maalfrid_npd                          | 2,657,179     | 10,989      | 241              |
| maalfrid_custompublish                | 2,493,062     | 9,404       | 265              |
| maalfrid_aldringoghelse               | 2,475,601     | 6,927       | 357              |
| maalfrid_bioteknologiradet            | 2,450,272     | 6,135       | 399              |
| maalfrid_nyemetoder                   | 2,426,982     | 10,999      | 220              |
| maalfrid_arbeidstilsynet              | 2,426,255     | 7,030       | 345              |
| maalfrid_riksantikvaren               | 2,300,159     | 8,933       | 257              |
| maalfrid_sjt                          | 2,292,578     | 11,455      | 200              |
| lovdata_cd_lokaleforskrifter_2005     | 2,233,543     | 22,824      | 97               |
| maalfrid_hvl                          | 2,194,063     | 9,604       | 228              |
| maalfrid_luftfartstilsynet            | 2,149,215     | 10,092      | 212              |
| maalfrid_dfo                          | 2,123,797     | 9,384       | 226              |
| maalfrid_ldo                          | 2,093,301     | 7,471       | 280              |
| maalfrid_kompetansenorge              | 1,997,363     | 10,496      | 190              |
| maalfrid_forbrukerradet               | 1,992,302     | 7,493       | 265              |
| maalfrid_himolde                      | 1,959,626     | 10,200      | 192              |
| maalfrid_usn                          | 1,828,928     | 7,553       | 242              |
| lovdata_cd_norgeslover_2005           | 1,802,578     | 1,419       | 1,270            |
| maalfrid_naku                         | 1,786,086     | 5,328       | 335              |
| maalfrid_medietilsynet                | 1,648,462     | 6,758       | 243              |
| maalfrid_matematikksenteret           | 1,608,332     | 7,474       | 215              |
| maalfrid_diku                         | 1,579,996     | 6,383       | 247              |
| maalfrid_forskningsetikk              | 1,573,014     | 5,653       | 278              |
| maalfrid_godeidrettsanlegg            | 1,539,910     | 6,252       | 246              |
| maalfrid_dirmin                       | 1,500,122     | 5,427       | 276              |
| maalfrid_diskrimineringsnemnda        | 1,498,443     | 4,270       | 350              |
| maalfrid_naturfag                     | 1,481,316     | 6,108       | 242              |
| maalfrid_arbeidsretten                | 1,473,299     | 4,864       | 302              |
| lovdata_cd_rtv_rundskriv_2005         | 1,392,547     | 9,831       | 141              |
| maalfrid_fellesstudentsystem          | 1,392,117     | 10,553      | 131              |
| maalfrid_nupi                         | 1,322,743     | 5,628       | 235              |
| maalfrid_kriminalitetsforebygging     | 1,223,976     | 4,769       | 256              |
| maalfrid_anskaffelser                 | 1,214,995     | 5,602       | 216              |
| maalfrid_folketrygdfondet             | 1,212,747     | 4,347       | 278              |
| maalfrid_miljopakken                  | 1,195,869     | 5,634       | 212              |
| maalfrid_nih                          | 1,146,471     | 5,415       | 211              |
| lovdata_cd_skatt_rundskriv_2005       | 1,138,339     | 411         | 2,769            |
| maalfrid_statsbygg                    | 1,125,666     | 4,520       | 249              |
| maalfrid_nb                           | 1,085,457     | 4,251       | 255              |
| maalfrid_unit                         | 1,072,199     | 6,476       | 165              |
| maalfrid_npolar                       | 1,071,381     | 2,708       | 395              |
| maalfrid_valgdirektoratet             | 1,028,381     | 9,316       | 110              |
| maalfrid_barneombudet                 | 1,001,224     | 2,863       | 349              |
| maalfrid_datatilsynet                 | 990,582       | 3,018       | 328              |
| maalfrid_lottstift                    | 985,351       | 3,676       | 268              |
| maalfrid_aho                          | 977,116       | 4,637       | 210              |
| maalfrid_sykehuspartner               | 961,362       | 4,693       | 204              |
| maalfrid_naturfagsenteret             | 922,174       | 3,957       | 233              |
| maalfrid_khio                         | 869,917       | 3,457       | 251              |
| maalfrid_spesialenheten               | 845,989       | 2,188       | 386              |
| maalfrid_xn--miljlftet-o8ab           | 822,783       | 3,468       | 237              |
| maalfrid_samordnaopptak               | 805,644       | 2,415       | 333              |
| maalfrid_helsenorge                   | 802,003       | 3,116       | 257              |
| maalfrid_skrivesenteret               | 793,053       | 4,250       | 186              |
| maalfrid_mareano                      | 784,843       | 3,821       | 205              |
| maalfrid_fiskeridirektoratet          | 772,720       | 2,499       | 309              |
| maalfrid_sykehusinnkjop               | 754,616       | 4,440       | 169              |
| maalfrid_matportalen                  | 641,663       | 2,413       | 265              |
| maalfrid_spk                          | 621,687       | 2,181       | 285              |
| maalfrid_pasientsikkerhetsprogrammet  | 610,855       | 4,796       | 127              |
| maalfrid_justervesenet                | 607,767       | 1,946       | 312              |
| maalfrid_nhn                          | 594,591       | 3,665       | 162              |
| maalfrid_sshf                         | 589,448       | 1,950       | 302              |
| maalfrid_bibliotekutvikling           | 573,724       | 3,295       | 174              |
| maalfrid_nysgjerrigper                | 572,860       | 3,088       | 185              |
| maalfrid_nodnett                      | 549,483       | 2,743       | 200              |
| maalfrid_giek                         | 525,782       | 1,840       | 285              |
| maalfrid_une                          | 524,664       | 1,281       | 409              |
| maalfrid_samas                        | 512,469       | 2,610       | 196              |
| maalfrid_kriminalomsorgen             | 506,869       | 1,990       | 254              |
| maalfrid_kjonnsforskning              | 495,072       | 1,464       | 338              |
| lovdata_cd_rundskriv_lovavdeling_2005 | 482,605       | 419         | 1,151            |
| maalfrid_kunstkultursenteret          | 478,748       | 1,460       | 327              |
| maalfrid_nynorsksenteret              | 472,484       | 2,147       | 220              |
| maalfrid_ceres                        | 457,001       | 1,988       | 229              |
| maalfrid_stami                        | 456,707       | 1,190       | 383              |
| maalfrid_nsm                          | 452,597       | 1,573       | 287              |
| maalfrid_gjenopptakelse               | 430,682       | 1,501       | 286              |
| maalfrid_nfi                          | 430,469       | 1,557       | 276              |
| maalfrid_nidsenter                    | 416,329       | 1,657       | 251              |
| maalfrid_nasjonalmuseet               | 396,739       | 1,106       | 358              |
| maalfrid_forbrukertilsynet            | 395,317       | 1,252       | 315              |
| maalfrid_natursekken                  | 389,147       | 3,657       | 106              |
| maalfrid_fordelingsutvalget           | 362,923       | 1,416       | 256              |
| maalfrid_digdir                       | 358,558       | 2,159       | 166              |
| maalfrid_forsvaret                    | 339,218       | 1,243       | 272              |
| maalfrid_beccle                       | 337,729       | 1,554       | 217              |
| maalfrid_romsenter                    | 335,107       | 1,154       | 290              |
| maalfrid_geonorge                     | 306,914       | 1,658       | 185              |
| maalfrid_universell                   | 269,369       | 2,206       | 122              |
| maalfrid_ovf                          | 267,941       | 950         | 282              |
| maalfrid_forbrukereuropa              | 264,366       | 1,043       | 253              |
| maalfrid_politihogskolen              | 264,192       | 1,253       | 210              |
| maalfrid_vinmonopolet                 | 250,998       | 689         | 364              |
| maalfrid_energimerking                | 243,288       | 1,061       | 229              |
| maalfrid_ombudsmann                   | 235,226       | 432         | 544              |
| maalfrid_vea-fs                       | 231,109       | 1,293       | 178              |
| maalfrid_traumebevisst                | 228,320       | 2,482       | 91               |
| maalfrid_npe                          | 208,768       | 1,018       | 205              |
| maalfrid_pkh                          | 206,925       | 814         | 254              |
| maalfrid_opplaringslovutvalget        | 198,545       | 561         | 353              |
| maalfrid_helfo                        | 197,334       | 1,005       | 196              |
| maalfrid_regionaleforskningsfond      | 191,416       | 1,010       | 189              |
| maalfrid_nafkam                       | 180,622       | 582         | 310              |
| maalfrid_jernbanemagasinet            | 178,723       | 422         | 423              |
| maalfrid_polarhistorie                | 176,126       | 393         | 448              |
| maalfrid_aasentunet                   | 165,549       | 543         | 304              |
| maalfrid_riksteatret                  | 161,970       | 809         | 200              |
| maalfrid_realfagsloyper               | 160,310       | 765         | 209              |
| maalfrid_koro                         | 156,518       | 584         | 268              |
| maalfrid_squarespace                  | 149,259       | 515         | 289              |
| maalfrid_politietssikkerhetstjeneste  | 146,346       | 478         | 306              |
| maalfrid_unknown                      | 142,298       | 715         | 199              |
| maalfrid_whocc                        | 122,839       | 664         | 184              |
| maalfrid_konfliktraadet               | 122,030       | 379         | 321              |
| maalfrid_okokrim                      | 119,794       | 381         | 314              |
| maalfrid_brreg                        | 115,114       | 583         | 197              |
| maalfrid_riksmekleren                 | 113,287       | 570         | 198              |
| maalfrid_sismo                        | 112,976       | 316         | 357              |
| maalfrid_akkreditert                  | 101,275       | 513         | 197              |
| maalfrid_sivilforsvaret               | 101,178       | 528         | 191              |
| maalfrid_radetfordyreetikk            | 100,021       | 446         | 224              |
| maalfrid_lanekassen                   | 97,196        | 309         | 314              |
| maalfrid_digidel                      | 96,967        | 621         | 156              |
| maalfrid_uit                          | 92,451        | 612         | 151              |
| maalfrid_generaladvokaten             | 91,998        | 297         | 309              |
| maalfrid_nyinorge                     | 90,938        | 204         | 445              |
| maalfrid_lokforerskolen               | 90,255        | 478         | 188              |
| maalfrid_varsom                       | 87,050        | 576         | 151              |
| maalfrid_ffi                          | 82,147        | 224         | 366              |
| maalfrid_kulturminnefondet            | 81,683        | 424         | 192              |
| maalfrid_unesco                       | 78,677        | 388         | 202              |
| maalfrid_yrkesfisker                  | 76,760        | 512         | 149              |
| maalfrid_dekom                        | 74,066        | 1,331       | 55               |
| maalfrid_omsorgsforskning             | 73,528        | 332         | 221              |
| maalfrid_lektor2                      | 70,477        | 561         | 125              |
| maalfrid_openaccess                   | 65,385        | 197         | 331              |
| maalfrid_ssn                          | 64,111        | 308         | 208              |
| maalfrid_lokalhistorie                | 61,885        | 250         | 247              |
| maalfrid_laudim                       | 59,669        | 402         | 148              |
| maalfrid_nlb                          | 58,927        | 206         | 286              |
| maalfrid_riksadvokaten                | 57,938        | 156         | 371              |
| maalfrid_denkulturelleskolesekken     | 46,768        | 248         | 188              |
| maalfrid_sivilrett                    | 45,214        | 145         | 311              |
| maalfrid_htu                          | 43,778        | 171         | 256              |
| maalfrid_yr                           | 41,565        | 575         | 72               |
| maalfrid_informasjonskompetanse       | 40,989        | 334         | 122              |
| maalfrid_finansportalen               | 40,333        | 187         | 215              |
| maalfrid_dep                          | 38,882        | 126         | 308              |
| maalfrid_kulturped                    | 37,718        | 99          | 380              |
| maalfrid_feide                        | 37,583        | 274         | 137              |
| maalfrid_fug                          | 35,253        | 123         | 286              |
| maalfrid_kulturoghelse                | 34,762        | 189         | 183              |
| maalfrid_helseklage                   | 33,612        | 127         | 264              |
| maalfrid_nbsk                         | 31,334        | 215         | 145              |
| maalfrid_matogindustri                | 31,232        | 207         | 150              |
| maalfrid_sinn                         | 28,114        | 154         | 182              |
| maalfrid_transport21                  | 25,691        | 91          | 282              |
| maalfrid_vergemal                     | 24,189        | 80          | 302              |
| maalfrid_konkursradet                 | 24,072        | 78          | 308              |
| maalfrid_norec                        | 22,496        | 78          | 288              |
| maalfrid_pts                          | 21,346        | 81          | 263              |
| maalfrid_nasjonaleturistveger         | 20,237        | 111         | 182              |
| maalfrid_hjelpelinjen                 | 19,476        | 86          | 226              |
| maalfrid_iearth                       | 19,418        | 150         | 129              |
| maalfrid_russamtalen                  | 19,035        | 69          | 275              |
| maalfrid_xn--kvinneligomskjring-1ub   | 18,607        | 79          | 235              |
| maalfrid_memu                         | 17,820        | 101         | 176              |
| maalfrid_nynorskbok                   | 17,769        | 98          | 181              |
| maalfrid_regjeringsadvokaten          | 17,416        | 55          | 316              |
| maalfrid_xn--forskerfr-t8a            | 16,827        | 177         | 95               |
| maalfrid_xn--tilbakefring-2jb         | 15,814        | 49          | 322              |
| maalfrid_ringerikefengsel             | 15,669        | 28          | 559              |
| maalfrid_skattefunn                   | 15,625        | 54          | 289              |
| maalfrid_skeivtarkiv                  | 15,537        | 69          | 225              |
| maalfrid_fordelingsutvalet            | 15,473        | 35          | 442              |
| maalfrid_samfunnskunnskap             | 15,110        | 60          | 251              |
| maalfrid_shiprep                      | 14,632        | 146         | 100              |
| maalfrid_sevuppt                      | 14,087        | 55          | 256              |
| maalfrid_haldenfengsel                | 13,655        | 38          | 359              |
| maalfrid_forbrukerklageutvalget       | 13,472        | 51          | 264              |
| maalfrid_mhfa                         | 12,591        | 146         | 86               |
| maalfrid_ah                           | 11,787        | 36          | 327              |
| maalfrid_nettvett                     | 11,353        | 44          | 258              |
| maalfrid_uh-it                        | 11,158        | 281         | 39               |
| maalfrid_fishgen                      | 10,318        | 29          | 355              |
| maalfrid_designavgang                 | 10,164        | 75          | 135              |
| maalfrid_global                       | 9,363         | 43          | 217              |
| maalfrid_valg                         | 8,797         | 48          | 183              |
| maalfrid_havmiljo                     | 8,734         | 69          | 126              |
| maalfrid_altinn                       | 7,945         | 50          | 158              |
| maalfrid_miljoklagenemnda             | 7,797         | 35          | 222              |
| maalfrid_spinn-inn                    | 7,699         | 48          | 160              |
| maalfrid_kantinekurset                | 7,397         | 54          | 136              |
| maalfrid_bastoyfengsel                | 7,142         | 56          | 127              |
| maalfrid_norskpetroleum               | 6,107         | 120         | 50               |
| maalfrid_voldsoffererstatning         | 6,079         | 27          | 225              |
| maalfrid_musikkbasertmiljobehandling  | 5,186         | 39          | 132              |
| maalfrid_prosjektveiviseren           | 5,154         | 15          | 343              |
| maalfrid_aldersvennlig                | 4,919         | 32          | 153              |
| maalfrid_barentswatch                 | 4,829         | 32          | 150              |
| maalfrid_fmfiavo@fylkesmannen         | 4,740         | 69          | 68               |
| maalfrid_kk-utvalget                  | 4,697         | 19          | 247              |
| maalfrid_agropub                      | 4,434         | 17          | 260              |
| maalfrid_utdanningiverden             | 4,369         | 14          | 312              |
| maalfrid_overgangsbolig               | 3,862         | 36          | 107              |
| maalfrid_forsvaretsmuseer             | 3,840         | 35          | 109              |
| maalfrid_okopark                      | 3,282         | 12          | 273              |
| maalfrid_pst                          | 2,866         | 14          | 204              |
| maalfrid_sikkerhverdag                | 2,786         | 19          | 146              |
| maalfrid_arkitektur                   | 2,436         | 15          | 162              |
| maalfrid_velgekte                     | 2,287         | 10          | 228              |
| maalfrid_addlab                       | 2,109         | 12          | 175              |
| maalfrid_romerikefengsel              | 2,088         | 19          | 109              |
| maalfrid_utdanning                    | 2,009         | 12          | 167              |
| maalfrid_grunderskolen                | 1,994         | 7           | 284              |
| maalfrid_umb                          | 1,958         | 9           | 217              |
| maalfrid_oslofengsel                  | 1,756         | 8           | 219              |
| maalfrid_hjorteviltregisteret         | 1,600         | 5           | 320              |
| maalfrid_alleteller                   | 1,511         | 7           | 215              |
| maalfrid_webhuset                     | 1,409         | 5           | 281              |
| maalfrid_lykillinn                    | 1,349         | 4           | 337              |
| maalfrid_kulturfag                    | 1,215         | 6           | 202              |
| maalfrid_unimus                       | 940           | 4           | 235              |
| maalfrid_anleggsregisteret            | 928           | 5           | 185              |
| maalfrid_mangfoldsprisen              | 597           | 3           | 199              |
| maalfrid_algae2future                 | 456           | 8           | 57               |
| maalfrid_mammapresenterer             | 447           | 2           | 223              |
| maalfrid_karriereveiledning           | 391           | 27          | 14               |
| maalfrid_nodsms                       | 351           | 4           | 87               |
| maalfrid_kildekompasset               | 302           | 1           | 302              |
| maalfrid_praksisfou                   | 297           | 1           | 297              |
| maalfrid_retttilaalese                | 246           | 3           | 82               |
| maalfrid_indreostfoldfengsel          | 215           | 3           | 71               |
| maalfrid_xn--kroppsvingsforskning-gcc | 205           | 2           | 102              |
| maalfrid_pahoyden                     | 154           | 1           | 154              |
| maalfrid_norren                       | 42            | 1           | 42               |

### Languages
| Language   | Words         | Documents   | Words/Document   |
|-----------:|--------------:|------------:|-----------------:|
| no         | 2,899,156,476 | 5,551,136   | 522              |
| da         | 944,104,161   | 293,767     | 3,213            |
| en         | 476,390,897   | 1,466,330   | 324              |
| nn         | 181,310,112   | 492,410     | 368              |
| fr         | 50,297,424    | 107,935     | 465              |
| de         | 27,015,612    | 63,782      | 423              |
| sv         | 16,046,622    | 57,029      | 281              |
| es         | 8,573,155     | 31,661      | 270              |
| fi         | 4,792,837     | 16,471      | 290              |
| pt         | 2,547,144     | 14,952      | 170              |
| oc         | 2,170,769     | 4,988       | 435              |
| nl         | 1,911,626     | 7,355       | 259              |
| zh         | 1,495,995     | 7,797       | 191              |
| uk         | 1,474,032     | 4,451       | 331              |
| ca         | 1,390,667     | 3,664       | 379              |
| la         | 1,282,405     | 531         | 2,415            |
| it         | 1,280,422     | 6,903       | 185              |
| ru         | 1,233,667     | 5,880       | 209              |
| et         | 1,059,537     | 4,042       | 262              |
| cs         | 935,395       | 4,363       | 214              |
| eu         | 851,593       | 3,170       | 268              |
| pl         | 775,420       | 5,240       | 147              |
| fa         | 503,880       | 2,061       | 244              |
| ja         | 350,838       | 3,597       | 97               |
| is         | 311,519       | 1,004       | 310              |
| id         | 223,591       | 1,297       | 172              |
| ar         | 212,495       | 1,183       | 179              |
| hu         | 192,959       | 1,378       | 140              |
| vi         | 137,056       | 639         | 214              |
| so         | 131,743       | 605         | 217              |
| el         | 120,726       | 620         | 194              |
| hr         | 111,859       | 513         | 218              |
| lv         | 106,155       | 64          | 1,658            |
| sl         | 94,417        | 706         | 133              |
| tr         | 91,459        | 1,051       | 87               |
| ro         | 80,974        | 446         | 181              |
| eo         | 80,688        | 506         | 159              |
| lt         | 67,977        | 581         | 117              |
| sr         | 66,429        | 793         | 83               |
| gl         | 65,922        | 594         | 110              |
| war        | 56,846        | 235         | 241              |
| ko         | 56,147        | 924         | 60               |
| th         | 54,677        | 364         | 150              |
| am         | 46,477        | 327         | 142              |
| ceb        | 35,679        | 272         | 131              |
| ml         | 35,503        | 153         | 232              |
| sq         | 32,258        | 158         | 204              |
| tl         | 31,094        | 164         | 189              |
| kk         | 27,819        | 70          | 397              |
| mn         | 21,540        | 22          | 979              |
| sw         | 18,629        | 65          | 286              |
| pnb        | 18,502        | 81          | 228              |
| sk         | 17,642        | 198         | 89               |
| bg         | 17,142        | 98          | 174              |
| gu         | 16,973        | 13          | 1,305            |
| ur         | 16,017        | 146         | 109              |
| sh         | 15,007        | 130         | 115              |
| mk         | 13,479        | 65          | 207              |
| ckb        | 9,350         | 44          | 212              |
| ku         | 9,058         | 54          | 167              |
| az         | 8,003         | 51          | 156              |
| ast        | 7,910         | 63          | 125              |
| uz         | 6,883         | 35          | 196              |
| ta         | 4,177         | 59          | 70               |
| ms         | 3,817         | 126         | 30               |
| fy         | 3,579         | 28          | 127              |
| hy         | 3,478         | 34          | 102              |
| pa         | 3,283         | 16          | 205              |
| hi         | 2,812         | 41          | 68               |
| bo         | 2,551         | 1           | 2,551            |
| ht         | 2,534         | 11          | 230              |
| be         | 2,479         | 44          | 56               |
| min        | 2,155         | 7           | 307              |
| jv         | 2,067         | 38          | 54               |
| cy         | 1,993         | 42          | 47               |
| su         | 1,845         | 24          | 76               |
| ps         | 1,832         | 15          | 122              |
| als        | 1,826         | 41          | 44               |
| bn         | 1,799         | 21          | 85               |
| af         | 1,706         | 21          | 81               |
| bs         | 1,524         | 24          | 63               |
| nds        | 1,492         | 88          | 16               |
| qu         | 1,484         | 13          | 114              |
| my         | 1,115         | 16          | 69               |
| ga         | 972           | 27          | 36               |
| mt         | 940           | 12          | 78               |
| si         | 907           | 23          | 39               |
| te         | 853           | 17          | 50               |
| ilo        | 801           | 16          | 50               |
| km         | 690           | 12          | 57               |
| io         | 689           | 10          | 68               |
| tt         | 675           | 20          | 33               |
| jbo        | 621           | 27          | 23               |
| gn         | 595           | 7           | 85               |
| as         | 584           | 2           | 292              |
| ug         | 581           | 6           | 96               |
| kv         | 562           | 3           | 187              |
| br         | 553           | 23          | 24               |
| kn         | 531           | 19          | 27               |
| pam        | 476           | 1           | 476              |
| he         | 396           | 14          | 28               |
| kw         | 329           | 5           | 65               |
| ka         | 326           | 17          | 19               |
| vep        | 309           | 15          | 20               |
| yo         | 261           | 5           | 52               |
| ky         | 232           | 11          | 21               |
| azb        | 216           | 1           | 216              |
| ba         | 203           | 5           | 40               |
| wa         | 191           | 21          | 9                |
| gom        | 164           | 9           | 18               |
| tg         | 129           | 3           | 43               |
| ia         | 125           | 11          | 11               |
| mr         | 122           | 6           | 20               |
| lmo        | 90            | 24          | 3                |
| pms        | 75            | 10          | 7                |
| lb         | 68            | 15          | 4                |
| rue        | 67            | 2           | 33               |
| vec        | 67            | 3           | 22               |
| ne         | 51            | 5           | 10               |
| hsb        | 51            | 2           | 25               |
| cbk        | 46            | 2           | 23               |
| or         | 44            | 2           | 22               |
| ie         | 38            | 5           | 7                |
| tk         | 36            | 4           | 9                |
| eml        | 31            | 4           | 7                |
| bar        | 31            | 3           | 10               |
| arz        | 31            | 1           | 31               |
| sco        | 30            | 1           | 30               |
| gd         | 29            | 2           | 14               |
| li         | 22            | 3           | 7                |
| lrc        | 20            | 1           | 20               |
| diq        | 20            | 2           | 10               |
| dsb        | 19            | 1           | 19               |
| yue        | 19            | 1           | 19               |
| os         | 15            | 2           | 7                |
| nah        | 14            | 2           | 7                |
| mg         | 14            | 2           | 7                |
| wuu        | 14            | 1           | 14               |
| sd         | 14            | 1           | 14               |
| cv         | 12            | 1           | 12               |
| scn        | 9             | 2           | 4                |
| bh         | 8             | 1           | 8                |
| bcl        | 8             | 1           | 8                |
| new        | 4             | 1           | 4                |
| ce         | 4             | 1           | 4                |
| vo         | 3             | 2           | 1                |
| gv         | 3             | 1           | 3                |
| frr        | 3             | 1           | 3                |
| mzn        | 3             | 1           | 3                |
| lo         | 2             | 1           | 2                |

### Publish Periode
|   Decade | Words         | Documents   | Words/Document   |
|---------:|--------------:|------------:|-----------------:|
|     2020 | 3,640,555,163 | 7,486,987   | 672              |
|     2010 | 49,596,905    | 206,107     | 2,383            |
|     2000 | 76,215,035    | 89,416      | 10,668           |
|     1990 | 122,831,827   | 29,979      | 69,912           |
|     1980 | 53,794,156    | 55,215      | 9,877            |
|     1970 | 33,995,516    | 55,533      | 6,593            |
|     1960 | 35,981,142    | 87,285      | 4,469            |
|     1950 | 40,527,060    | 113,384     | 3,597            |
|     1940 | 36,906,757    | 42,049      | 15,702           |
|     1930 | 36,535,860    | 716         | 507,173          |
|     1920 | 52,070,676    | 1,087       | 483,201          |
|     1910 | 63,920,279    | 1,255       | 501,227          |
|     1900 | 61,593,361    | 1,164       | 525,050          |
|     1890 | 88,616,464    | 1,814       | 485,506          |
|     1880 | 59,549,399    | 1,087       | 550,945          |
|     1870 | 26,541,488    | 634         | 406,854          |
|     1860 | 39,854,074    | 710         | 543,956          |
|     1850 | 55,078,195    | 864         | 635,165          |
|     1840 | 31,307,769    | 534         | 583,077          |
|     1830 | 18,377,415    | 374         | 479,400          |
|     1820 | 4,821,598     | 147         | 339,040          |
|     1810 | 1,013,747     | 58          | 130,214          |


### Discussion of Biases
Please refer to our papers.

### Dataset Curators
[Freddy Wetjen](mailto:Freddy.wetjen@nb.no) and [Per Egil Kummervold](mailto:Per.Kummervold@nb.no)


## License
Various licences applies to different parts of the corpus. Every document in the corpus has a tag telling what **"doc_type"** it belongs to. If you are unable to accept any of the licenses, you should filter out the **"doc_type"** with a conflicting license. 

| Doc_type  | License  | 
| :-------- | :------------- |  
| government_nb, government_nn, parliament, publicreports, lovdata_cd_\*, maalfrid_\* | [NLOD 2.0](https://data.norge.no/nlod/en/2.0/)|
| newspapers_ocr, newspapers_pdf, books| [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)|
| newspapers_online_nb, newspapers_online_nn | [CC BY-NC 2.0](https://creativecommons.org/licenses/by-nc/2.0/)|
| opensubtitles, wikipedia | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)
|

### Citation Information
If you are using the corpus, please refer to the articles below:
```
@inproceedings{kummervold-etal-2022-norwegian-colossal,
  title     = {The {N}orwegian colossal corpus: A text corpus for training large {N}orwegian language models},
  author    = {Kummervold, Per E  and
               Wetjen, Freddy    and
               De la Rosa, Javier},
  booktitle = {Proceedings of the Thirteenth Language Resources and Evaluation Conference (LREC)},
  year      = {2022},
  address   = {Marseille, France},
  publisher = {European Language Resources Association},
  url       = {https://aclanthology.org/2022.lrec-1.410},
  pages     = {3852--3860},
  abstract  = {Norwegian has been one of many languages lacking sufficient available text to train quality language models. In an attempt to bridge this gap, we introduce the Norwegian Colossal Corpus (NCC), which comprises 49GB of clean Norwegian textual data containing over 7B words. The NCC is composed of different and varied sources, ranging from books and newspapers to government documents and public reports, showcasing the various uses of the Norwegian language in society. The corpus contains mainly Norwegian Bokmål and Norwegian Nynorsk. Each document in the corpus is tagged with metadata that enables the creation of sub-corpora for specific needs. Its structure makes it easy to combine with large web archives that for licensing reasons could not be distributed together with the NCC. By releasing this corpus openly to the public, we hope to foster the creation of both better Norwegian language models and multilingual language models with support for Norwegian.},
}

@inproceedings{kummervold-etal-2021-operationalizing,
  title     = {Operationalizing a National Digital Library: The Case for a {N}orwegian Transformer Model},
  author    = {Kummervold, Per E  and
               De la Rosa, Javier  and
               Wetjen, Freddy  and
               Brygfjeld, Svein Arne},
  booktitle = {Proceedings of the 23rd Nordic Conference on Computational Linguistics (NoDaLiDa)},
  year      = {2021},
  address   = {Reykjavik, Iceland (Online)},
  publisher = {Linköping University Electronic Press, Sweden},
  url       = {https://aclanthology.org/2021.nodalida-main.3},
  pages     = {20--29},
  abstract  = {In this work, we show the process of building a large-scale training set from digital and digitized collections at a national library.
  The resulting Bidirectional Encoder Representations from Transformers (BERT)-based language model for Norwegian outperforms multilingual BERT (mBERT) models
  in several token and sequence classification tasks for both Norwegian Bokmål and Norwegian Nynorsk. Our model also improves the mBERT performance for other
  languages present in the corpus such as English, Swedish, and Danish. For languages not included in the corpus, the weights degrade moderately while keeping strong multilingual properties. Therefore,
  we show that building high-quality models within a memory institution using somewhat noisy optical character recognition (OCR) content is feasible, and we hope to pave the way for other memory institutions to follow.},
}
```