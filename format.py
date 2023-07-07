from data import FormatType, UseArea
import matplotlib.pyplot as plt


class Format:
    def __init__(self, typeFormat: FormatType, releaseDate: int, useArea: UseArea):
        self.typeFormat = typeFormat
        self.releaseDate = releaseDate
        self.useArea = useArea


newFormat = Format(FormatType.CSV, 2020, UseArea.SPREAD_SHEET)

dataSet = [
    Format(FormatType.CSV, 1983, UseArea.SPREAD_SHEET),
    Format(FormatType.ASN_1, 1984, UseArea.TELECAMMUNNICATION),
    Format(FormatType.XML, 1996, UseArea.WEB_APPLICATION),
    Format(FormatType.PROCOLE_BUFFERS, 2001, UseArea.DISTRIBUTED_COMPUTING),
    Format(FormatType.JSON, 2006, UseArea.WEB_APPLICATION),
    Format(FormatType.APACHE_THRIFT, 2006, UseArea.DISTRIBUTED_COMPUTING),
    Format(FormatType.MASSAGE_PACK, 2009, UseArea.DISTRIBUTED_COMPUTING),
    Format(FormatType.BSON, 2010, UseArea.DATABASES),
    Format(FormatType.MICROSOFT_BOND, 2011, UseArea.DISTRIBUTED_COMPUTING),
    Format(FormatType.TOML, 2013, UseArea.SOFTWARE_CONFIGURATION),
    Format(FormatType.CBOR, 2013, UseArea.INTERNET_OF_THINGS),
    Format(FormatType.CAPTN_PROTO, 2013, UseArea.DISTRIBUTED_COMPUTING),
    Format(FormatType.FLAT_BUFFERS, 2014, UseArea.GAMES),
    Format(FormatType.FLEX_BUFFERS, 2016, UseArea.GAMES),
]

fiagramData = list(
    map(
        lambda x: {
            "abscisse": x.useArea.value,
            "ordonne": x.releaseDate,
            "value": x.typeFormat.value,
        },
        dataSet,
    )
)

abscisse = [obj["abscisse"] for obj in fiagramData]
ordonne = [obj["ordonne"] for obj in fiagramData]
values = [obj["value"] for obj in fiagramData]

unique_values = list(set(values))
color_map = plt.cm.get_cmap("tab20", len(unique_values))

plt.scatter(
    abscisse,
    ordonne,
    c=[unique_values.index(value) for value in values],
    cmap=color_map,
    # marker="^",
    # marker="s",
)

for i, txt in enumerate(values):
    plt.annotate(
        txt,
        (abscisse[i], ordonne[i]),
        xytext=(5, 5),
        textcoords="offset points",
        fontsize=7,
    )

plt.xlabel("Domaines d'utilisation")
plt.ylabel("Années de sortie")
plt.title("Représentation des formats de données")
plt.xticks(fontsize=7, rotation=10)

plt.colorbar(ticks=range(len(unique_values)), label="Values")


plt.show()
