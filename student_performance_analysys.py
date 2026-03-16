{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNFFu77D2DPWqZFX1s2vSbh"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 102,
      "metadata": {
        "id": "f2040SwMLdN-"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "\n",
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n",
        "import plotly.express as px"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.read_csv(\"student_performance_new.csv\")"
      ],
      "metadata": {
        "id": "emOTu-2Lezux"
      },
      "execution_count": 123,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.info()"
      ],
      "metadata": {
        "id": "noOlKVqGlC09"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.describe()"
      ],
      "metadata": {
        "id": "MQlmAU_bq2A0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df[\"grade\"] = df[\"grade\"].astype(str).str.strip().str.upper()\n",
        "\n",
        "grade_map = {\"A\":4, \"B\":3, \"C\":2, \"D\":1, \"F\":0}\n",
        "df[\"grade\"] = df[\"grade\"].map(grade_map)"
      ],
      "metadata": {
        "id": "N9ONVga2samP"
      },
      "execution_count": 127,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df[\"grade\"] = df[\"grade\"].astype(\"float\")\n",
        "df[\"total_score\"] = df[\"total_score\"].astype(\"float\")\n"
      ],
      "metadata": {
        "id": "QJ4_7d1pzruu"
      },
      "execution_count": 128,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.corr()"
      ],
      "metadata": {
        "id": "Dv4e7_83ucA-"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "score_df = df.groupby(\"grade\")[\"weekly_self_study_hours\"].mean().reset_index()\n",
        "sns.barplot(x=\"grade\", y=\"weekly_self_study_hours\", data=df)\n",
        "plt.ylabel(\"average_hours\")\n",
        "plt.show()\n",
        "\n",
        "score_df = df.groupby(\"grade\")[\"total_score\"].mean().reset_index()\n",
        "sns.barplot(x=\"grade\", y=\"total_score\", data=df)\n",
        "plt.ylabel(\"average_score\")\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "DI4VkOtB7nCv"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sns.regplot(x=\"weekly_self_study_hours\", y=\"total_score\", data=df, scatter_kws={\"alpha\": 0.1})\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "LTaK6fTr-FV9"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sns.regplot(x=\"attendance_percentage\", y=\"total_score\", data=df, scatter_kws={\"alpha\": 0.1})\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "_tEfvsLaHqNE"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "fig = px.histogram(df, x=\"grade\", nbins=5)\n",
        "fig.show()\n",
        "\n",
        "fig = px.histogram(df, x=\"total_score\", nbins=30)\n",
        "fig.show()"
      ],
      "metadata": {
        "id": "mTnBdFRo_3ao"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "correlation_matrix = df.corr()\n",
        "fig = px.imshow(correlation_matrix, text_auto=True, color_continuous_scale=\"RdBu_r\")\n",
        "fig.update_layout(width=800,height=800)\n",
        "fig.show()"
      ],
      "metadata": {
        "id": "lVadjvKCBaRP"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import statsmodels.api as sm\n",
        "\n",
        "x = df[[\"weekly_self_study_hours\", \"attendance_percentage\", \"class_participation\"]]\n",
        "y = df[\"total_score\"]\n",
        "\n",
        "x = sm.add_constant(x)\n",
        "\n",
        "model = sm.OLS(y, x).fit()\n",
        "\n",
        "print(model.summary())"
      ],
      "metadata": {
        "id": "zy6KHCSxDe7-"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}