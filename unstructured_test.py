from unstructured.partition.auto import partition
from unstructured.staging.base import elements_to_json, elements_from_json
from unstructured.staging.base import convert_to_dict

elements = partition("1_★투자신청의견서_마스킹인베스트먼트_블라인드_20240216_v1.4.docx")
print(elements)
count = 0
for element in elements[:5]:
    count+=1
    print(count, ':', element)


# tables = [el for el in elements if el.category == "Table"]
# print('This is TABLES#####################')
# print(tables[0].text)
# print(tables[0].metadata.text_as_html)
# print('###########################')
dicts = convert_to_dict(elements)
filename = "outputs2.json"
elements_to_json(elements, filename=filename)
elements = elements_from_json(filename=filename)