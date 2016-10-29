from dc_base_scrapers.geojson_scraper import RandomIdGeoJSONScraper


stations_url = "http://inspire.misoportal.com/geoserver/mid_sussex_district_council_msdc_3830_pollingstations_point/ows?service=WFS&version=1.1.1&request=GetFeature&outputFormat=json&srsName=EPSG%3A4326&typeNames=mid_sussex_district_council_msdc_3830_pollingstations_point"
districts_url = "http://inspire.misoportal.com/geoserver/mid_sussex_district_council_msdc_3830_pollingdistricts_polygon/ows?service=WFS&version=1.1.1&request=GetFeature&outputFormat=json&srsName=EPSG%3A4326&typeNames=mid_sussex_district_council_msdc_3830_pollingdistricts_polygon"
council_id = 'E07000228'


stations_scraper = RandomIdGeoJSONScraper(stations_url, council_id, 'utf-8', 'stations')
stations_scraper.scrape()
districts_scraper = RandomIdGeoJSONScraper(districts_url, council_id, 'utf-8', 'districts')
districts_scraper.scrape()
