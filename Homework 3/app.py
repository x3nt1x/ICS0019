import pandas
from pandas import DataFrame
import cartopy.crs as crs
import cartopy.feature as feature
import matplotlib.pyplot as pyplot
from matplotlib.lines import Line2D
import matplotlib.patheffects as effects


def get_direct_flight_data(file: str) -> DataFrame:
    return pandas.read_csv(file, delimiter=';')


def merge_flight_data(direct_flight: DataFrame) -> DataFrame:
    all_flight_data = pandas.read_csv('https://enos.itcollege.ee/~eikivi/python/kaug6pe/Koduylesanne3/airports.dat')
    fields = ['IATA', 'Longitude', 'Latitude']

    return pandas.merge(direct_flight, all_flight_data[fields], on='IATA', how='inner')


def get_starting_airport(flight_data: DataFrame, IATA: str) -> tuple[float, float]:
    city = flight_data.loc[flight_data['IATA'] == IATA]
    return city["Longitude"][0], city["Latitude"][0]


def add_flights(starting_airport: tuple[float, float], flight_data: DataFrame, lines_color: str) -> None:
    for city, IATA, longitude, latitude in flight_data.values:
        pyplot.plot([starting_airport[0], longitude], [starting_airport[1], latitude],
                    color=lines_color, linewidth=1, marker='o', transform=crs.Geodetic())

        pyplot.text(longitude, latitude, IATA, horizontalalignment='right', transform=crs.Geodetic(), weight="bold",
                    color='white', path_effects=[effects.withStroke(linewidth=2, foreground="black")])


def add_legend(axes: pyplot.axes) -> None:
    legend_elements = [Line2D([0], [0], label='2020 flight data', color='red', linewidth=3),
                       Line2D([0], [0], label='2023 flight data', color='green', linewidth=3)]

    axes.legend(handles=legend_elements, title='Legend', loc='upper left')


def create_image() -> None:
    direct_flight_data_2020 = get_direct_flight_data('otselennud20.csv')
    direct_flight_data_2023 = get_direct_flight_data('otselennud23.csv')

    flight_data_2020 = merge_flight_data(direct_flight_data_2020)
    flight_data_2023 = merge_flight_data(direct_flight_data_2023)

    starting_airport = get_starting_airport(flight_data_2020, "TLL")

    projection = crs.Miller()
    axes = pyplot.axes(projection=projection, title='Tallinn Airport flights 2020 - 2023')
    axes.set_extent([-23, 45, 20, 70])
    axes.stock_img()
    axes.add_feature(feature.COASTLINE, lw=2)
    axes.add_feature(feature.BORDERS)

    pyplot.gcf().set_size_inches(20, 10)

    add_flights(starting_airport, flight_data_2020, 'red')
    add_flights(starting_airport, flight_data_2023, 'green')

    add_legend(axes)

    pyplot.savefig("flights.png")


if __name__ == '__main__':
    create_image()
