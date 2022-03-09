from typing import Iterable, List

import altair as alt
import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import STOPWORDS, WordCloud

# Defaults for matplot lib
plt.rcParams["figure.figsize"] = (10, 7)


# Load and clean the data. For how the cleaning is done, see the cleaning notebook.
survey = pd.read_parquet('/workspaces/snowmass-attendance/clean_survey.parquet')

# Some colors ot help out
default_color = alt.value("#1f77b4")

# Setup for word clouds
all_stops = set(STOPWORDS)
all_stops.update(['will'])


def make_wordcloud(text_array_itr: Iterable, extra_stopwords: List[str] = []) -> WordCloud:
    width = 2000
    height = int(width*2/3)
    text_array = [t for t in text_array_itr if t is not None and isinstance(t, str) and len(t) > 0]
    stops = set(extra_stopwords)
    stops.update(all_stops)
    wordcloud = WordCloud(background_color=None,
                          mode='RGBA',
                          stopwords=stops,
                          width=width,
                          height=height) \
                .generate(" ".join(text_array))
    # wordcloud.to_file(f"../web/assets/images/frontier_{name}.png")
    return wordcloud


def plot_wordcloud(wc: WordCloud):
    plt.figure(figsize=(30,15))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()


def dump_words(t_array):
    'Helper function for dumping text from feedback - do not leave its use in any notebook checked in!!!'
    text = [t for t in t_array if t is not None and isinstance(t, str) and len(t) > 0]
    for t in text:
        print(t)


def build_attend(brush = None, selection = None):
    'Build a histo of people wanting to attend.'
    c = alt.Chart(data=survey, title="Would you attend?")
    if brush is not None:
        c = c.transform_filter(brush)

    color = default_color if selection is None else alt.condition(selection, default_color, alt.value('orange'))

    attend_histo = (
        c
        .transform_joinaggregate(total='count(*)')
        .transform_calculate(pct='1 / datum.total')
        .mark_bar()
        .encode(
            x=alt.X(shorthand="count(attend)"),
            y=alt.Y(shorthand="attend:N", title="", sort="-x"),
            color = color
        )
    )

    attend_text = (
        attend_histo.mark_text(align="right", dx=-3)
                    .encode(
                        text=alt.Text("sum(pct):Q", format=".0%"),
                        color=alt.value("white")
                    )
    )

    if selection is not None:
        attend_histo = attend_histo.add_selection(selection)

    return attend_histo + attend_text
