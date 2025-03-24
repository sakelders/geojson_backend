import geopandas, progressbar, requests, json, argparse


class UploadException(Exception):
    pass


class FeatureUploader:
    def __init__(self, create_endpoint):
        self._create_endpoint = create_endpoint

    def upload_single_feature(self, feature):
        coordinates = self._get_polygons_from_feature(feature)
        name = feature[0]

        polygon_data = {'type': 'MultiPolygon', 'coordinates': coordinates}
        request_data = {'name': name, 'polygons': polygon_data}
        json_data = json.dumps(request_data)

        headers = {"Content-Type": "application/json"}
        response = requests.post(self._create_endpoint, data=json_data, headers=headers)

        if not response.ok:
            raise UploadException(response.reason)

    def _get_coordinates_from_polygon(self, polygon):
        exterior_coordinates = [(lat, lon) for lat, lon in polygon.exterior.coords]
        coordinates_lists = [exterior_coordinates]
        for interior in polygon.interiors:
            coordinates_lists.append([(lat, lon) for lat, lon in interior.coords])
        return coordinates_lists

    def _get_polygons_from_feature(self, feature):
        multipolygon = feature[1]
        polygons = multipolygon.geoms
        return list(map(self._get_coordinates_from_polygon, polygons))

def upload_data(data_filename, create_endpoint):
    uploader = FeatureUploader(create_endpoint)
    data = geopandas.read_file(data_filename)

    widgets = [progressbar.Bar('*')]
    bar = progressbar.ProgressBar(maxval=len(data.values), widgets=widgets).start()

    for i, feature in enumerate(data.values):
        uploader.upload_single_feature(feature)
        bar.update(i)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Upload municipality data.')
    parser.add_argument('data_filename', type=str,
                        help='The source file containing GeoJson municipality data.')
    parser.add_argument('url', type=str,
                        help='The url to send the upload request to.')

    print('Uploading data')

    args = parser.parse_args()
    upload_data(args.data_filename, args.url)

    print('\nUpload finished')