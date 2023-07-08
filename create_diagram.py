from data import FormatType, UseArea, Figure
import matplotlib.pyplot as plt


class Format:
    def __init__(
        self,
        typeFormat: FormatType,
        releaseDate: int,
        useArea: UseArea,
        mark: Figure,
        markColor: str,
    ):
        self.typeFormat = typeFormat
        self.releaseDate = releaseDate
        self.useArea = useArea
        self.mark = mark
        self.markColor = markColor


dataSet = [
    Format(FormatType.CSV, 1983, UseArea.SPREAD_SHEET, Figure.SQUARE, "#F6A901"),
    Format(
        FormatType.ASN_1, 1984, UseArea.TELECAMMUNNICATION, Figure.CIRCLE, "#C80058"
    ),
    Format(
        FormatType.XML, 1996, UseArea.WEB_APPLICATION, Figure.TRIANGLE_DOWN, "#007200"
    ),
    Format(
        FormatType.JSON, 2006, UseArea.WEB_APPLICATION, Figure.TRIANGLE_UP, "#008BFF"
    ),
    Format(
        FormatType.TOML, 2013, UseArea.SOFTWARE_CONFIGURATION, Figure.CIRCLE, "#DF56EA"
    ),
    Format(
        FormatType.YAML, 2000, UseArea.SOFTWARE_CONFIGURATION, Figure.CIRCLE, "#02BEAF"
    ),
    Format(
        FormatType.APACHE_AVRO, 2009, UseArea.BIG_DATA, Figure.TRIANGLE_UP, "#C53A00"
    ),
    Format(FormatType.BSON, 2010, UseArea.DATABASES, Figure.TRIANGLE_DOWN, "#FC8D82"),
    Format(FormatType.CBOR, 2013, UseArea.INTERNET_OF_THINGS, Figure.SQUARE, "#5D4CE8"),
    Format(FormatType.FLAT_BUFFERS, 2014, UseArea.GAMES, Figure.CIRCLE, "#02C6FF"),
    Format(FormatType.FLEX_BUFFERS, 2016, UseArea.GAMES, Figure.TRIANGLE_UP, "#898402"),
    Format(
        FormatType.PROCOLE_BUFFERS,
        2001,
        UseArea.DISTRIBUTED_COMPUTING,
        Figure.TRIANGLE_UP,
        "#FF00BD",
    ),
    Format(
        FormatType.APACHE_THRIFT,
        2006,
        UseArea.DISTRIBUTED_COMPUTING,
        Figure.TRIANGLE_DOWN,
        "#FFB14C",
    ),
    Format(
        FormatType.MASSAGE_PACK,
        2009,
        UseArea.DISTRIBUTED_COMPUTING,
        Figure.CIRCLE,
        "#B265FB",
    ),
    Format(
        FormatType.MICROSOFT_BOND,
        2011,
        UseArea.DISTRIBUTED_COMPUTING,
        Figure.TRIANGLE_DOWN,
        "#F8DD00",
    ),
    Format(
        FormatType.CAPTN_PROTO,
        2013,
        UseArea.DISTRIBUTED_COMPUTING,
        Figure.SQUARE,
        "#BDBDBD",
    ),
]

figureDate = list(
    map(
        lambda x: {
            "abscisse": x.useArea.value,
            "ordonne": x.releaseDate,
            "value": x.typeFormat.value,
            "mark": x.mark.value,
        },
        dataSet,
    )
)

abscisse = [obj["abscisse"] for obj in figureDate]
ordonne = [obj["ordonne"] for obj in figureDate]
marks = [obj["mark"] for obj in figureDate]


def BuildDiagram(plt, abscisses, ordonnes):
    plt.scatter(
        abscisse,
        ordonne,
        marker="",
    )

    plt.grid(True, linestyle="dashed", color="#d6d6d6", linewidth=0.5)

    plt.xlabel("Domaines d'utilisation")
    plt.ylabel("Années de sortie")
    plt.title("Représentation des formats de données")
    plt.xticks(fontsize=7, rotation=10)


def MarkDatasetElements(plt, dataset):
    for i, txt in enumerate(dataSet):
        plt.plot(
            abscisse[i],
            ordonne[i],
            marker=marks[i],
            markersize=7,
            color=dataSet[i].markColor,
        )
        plt.annotate(
            dataSet[i].typeFormat.value,
            (abscisse[i], ordonne[i]),
            xytext=(5, 5),
            textcoords="offset points",
            fontsize=7,
            # color=dataSet[i].markColor,
        )


BuildDiagram(plt, abscisse, ordonne)
MarkDatasetElements(plt, dataSet)

plt.show()
