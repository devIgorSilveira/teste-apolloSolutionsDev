import requests
import pandas as pd
import json

packages_names = [
    "standalone",
    "fablib",
    "unittest-expander",
    "tessera-client",
    "saltext.vmware",
    "botocore-a-la-carte-sagemaker-edge",
    "phil",
    "touca-fbs",
    "aoe2de-rms-gen-obj-parser",
    "git-search-replace",
    "jira-helper",
    "django-pg-zero-downtime-migrations",
    "pypairtree",
    "filediffs",
    "kb4.py",
    "panda-robot-client",
    "raol-libpyhtonpro",
    "nova-graph",
    "nose-detecthttp",
    "genetictabler",
    "labelord-halfdeadpie",
    "PyWinCtl",
    "times",
    "jinjamodificado",
    "baker",
    "zake",
    "alibabacloud-gateway-dingtalk-py2",
    "BoxArchive",
    "elv",
    "docker-zabbix-sender",
    "OpenDartReader",
    "django-polyfield",
    "resdk",
    "antchain-goodschain",
    "django-activitysync",
    "django-uwsgi-taskmanager",
    "reactive-pyecharts",
    "aliyun-python-sdk-nas",
    "tendril-projects",
    "tencentcloud-sdk-python-intlpartnersmgt",
    "CodeViking.contracts",
    "matrix-array",
    "custom-e-celery",
    "nameko-neo4j",
    "tlvdict",
    "zenfilter",
    "maze",
    "aliyun-python-sdk-ccc",
    "django-rest-utils-mosoti",
    "saudiaddress",
]

dict_nexessary_info = {
    "name": [],
    "last_version": [],
    "python_version": [],
    "downloads": [],
}

for name in packages_names:
    package = requests.get(f"https://pypi.org/pypi/{name}/json")

    dict_package = json.loads(package.content)

    actual_version = dict_package["info"]["version"]

    dict_nexessary_info["name"].append([dict_package["info"]["name"]])
    dict_nexessary_info["last_version"].append(
        [dict_package["releases"][actual_version][0]["upload_time"]]
    )
    dict_nexessary_info["python_version"].append(
        [dict_package["releases"][actual_version][0]["python_version"]]
    )
    dict_nexessary_info["downloads"].append(
        [dict_package["releases"][actual_version][0]["downloads"]]
    )


df_package = pd.DataFrame(dict_nexessary_info)

df_package.to_csv("pypi_packages.csv", index=False, sep=";")
