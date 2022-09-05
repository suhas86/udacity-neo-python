"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """

    neos = []
    with open(neo_csv_path, "r") as neo_file:
        reader = csv.DictReader(neo_file)
        for row in reader:
            designation = row['pdes']
            name = row['name'] or None
            diameter = float(row["diameter"]) if row["diameter"] else None
            hazardous = False if row["pha"] in ["", "N"] else True
            neo = NearEarthObject(
                designation=designation, name=name, diameter=diameter, hazardous=hazardous)
            neos.append(neo)
    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """

    approaches = []
    with open(cad_json_path, "r") as cad_file:
        reader = json.load(cad_file)
        cad_data = [dict(zip(reader["fields"], data))
                    for data in reader["data"]]
        for data in cad_data:
            designation = data['des']
            time = data['cd']
            distance = float(data['dist'])
            velocity = float(data['v_rel'])
            cad = CloseApproach(designation=designation,
                                time=time, distance=distance, velocity=velocity)
            approaches.append(cad)
    return approaches
