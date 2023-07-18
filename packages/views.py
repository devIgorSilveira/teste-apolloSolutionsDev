from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
from .utils import orderByName, orderByDownloads, orderByPython, orderByRelease


class PackageView(APIView):
    def get(self, request):
        is_ordered_by_name = request.query_params.get("name", None)
        is_ordered_by_release = request.query_params.get("release", None)
        is_ordered_by_python = request.query_params.get("python", None)
        is_ordered_by_download = request.query_params.get("download", None)

        packages = pd.read_csv("./pypi_packages.csv")

        packages_list = []

        for package in packages["name;last_version;python_version;downloads"]:
            splited_list = (
                package.replace("[", "").replace("]", "").replace("'", "").split(";")
            )
            packages_list.append(
                {
                    "name": splited_list[0],
                    "release_date": splited_list[1],
                    "python_version": splited_list[2],
                    "downloads": splited_list[3],
                }
            )

        if is_ordered_by_name:
            packages_list.sort(key=orderByName)
        elif is_ordered_by_release:
            packages_list.sort(key=orderByRelease, reverse=True)
        elif is_ordered_by_python:
            packages_list.sort(key=orderByPython, reverse=True)
        elif is_ordered_by_download:
            packages_list.sort(key=orderByDownloads)

        return Response({"packages": packages_list})


class PackageViewDetailByName(APIView):
    def get(self, request, name):
        packages = pd.read_csv("./pypi_packages.csv")

        packages_list = []

        for package in packages["name;last_version;python_version;downloads"]:
            splited_list = (
                package.replace("[", "").replace("]", "").replace("'", "").split(";")
            )
            packages_list.append(
                {
                    "name": splited_list[0],
                    "release_date": splited_list[1],
                    "python_version": splited_list[2],
                    "downloads": splited_list[3],
                }
            )

        index = packages_list.index(name)

        return Response({"package": packages_list[index]})
