{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPcWgXVGW2CjBPEDvdttuVJ",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Fjc2032/homework/blob/main/hw1ex2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nX_NNCmUfGVN",
        "outputId": "7ad022b6-6c44-4151-910f-bccf2f8b93e1"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "First number: 6\n",
            "Second number: 5\n",
            "Enter calculation type: +\n",
            "6  +  5  =  11\n"
          ]
        }
      ],
      "source": [
        "#HW 1 exercise 2\n",
        "a = int(input(\"First number: \"))\n",
        "\n",
        "b = int(input(\"Second number: \"))\n",
        "\n",
        "c = input(\"Enter calculation type: \")\n",
        "\n",
        "while(True):\n",
        "  if c == '+':\n",
        "\n",
        "    print(a, \" + \", b, \" = \", a + b)\n",
        "\n",
        "  elif c == '-':\n",
        "    print(a, \" - \", b, \" = \", a - b)\n",
        "\n",
        "  elif c == '*':\n",
        "    print (a, \" * \", b, \" = \", a * b)\n",
        "\n",
        "  elif c == '/':\n",
        "    print (a, \"/\", b, \" = \", a / b)\n",
        "\n",
        "  else:\n",
        "    print(\"Error.\")\n",
        "\n",
        "  break\n",
        "\n"
      ]
    }
  ]
}