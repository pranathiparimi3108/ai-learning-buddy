{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNZWHeRiDmLtXz5AxmAIp1k",
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
        "<a href=\"https://colab.research.google.com/github/pranathiparimi3108/ai-learning-buddy/blob/main/Untitled4.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "p956iE7UsB5y",
        "outputId": "48a885bd-b572-4ebb-b706-cc2cfdfe0f33"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m55.8/55.8 kB\u001b[0m \u001b[31m2.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m10.3/10.3 MB\u001b[0m \u001b[31m76.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m984.2/984.2 kB\u001b[0m \u001b[31m48.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m11.4/11.4 MB\u001b[0m \u001b[31m98.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h"
          ]
        }
      ],
      "source": [
        "!pip install -q -U streamlit google-genai pyngrok"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile app.py\n",
        "\n",
        "import streamlit as st\n",
        "from google import genai\n",
        "\n",
        "# Replace with your Gemini API key\n",
        "client = genai.Client(\n",
        "    api_key=st.secrets[\"GEMINI_API_KEY\"]\n",
        ")\n",
        "\n",
        "st.set_page_config(\n",
        "    page_title=\"AI Learning Buddy\",\n",
        "    page_icon=\"🎓\"\n",
        ")\n",
        "\n",
        "st.title(\"🎓 AI Learning Buddy\")\n",
        "\n",
        "topic = st.text_input(\"Enter a Topic\")\n",
        "\n",
        "option = st.selectbox(\n",
        "    \"Choose Activity\",\n",
        "    [\n",
        "        \"Explain Concept\",\n",
        "        \"Real-Life Example\",\n",
        "        \"Generate Quiz\",\n",
        "        \"Ask Anything\"\n",
        "    ]\n",
        ")\n",
        "\n",
        "if st.button(\"Generate\"):\n",
        "\n",
        "    if topic.strip() == \"\":\n",
        "        st.warning(\"Please enter a topic.\")\n",
        "\n",
        "    else:\n",
        "\n",
        "        if option == \"Explain Concept\":\n",
        "            prompt = f\"Explain {topic} in simple language for a beginner.\"\n",
        "\n",
        "        elif option == \"Real-Life Example\":\n",
        "            prompt = f\"Give one simple real-life example of {topic}.\"\n",
        "\n",
        "        elif option == \"Generate Quiz\":\n",
        "            prompt = f\"Create 5 MCQs on {topic} with answers.\"\n",
        "\n",
        "        else:\n",
        "            prompt = topic\n",
        "\n",
        "        response = client.models.generate_content(\n",
        "            model=\"gemini-flash-latest\",\n",
        "            contents=prompt\n",
        "        )\n",
        "\n",
        "        st.write(response.text)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "x7p4xSQ5sJ1U",
        "outputId": "78c62b97-a3cd-4827-aae3-57de9f1fca4d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing app.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pkill -f streamlit"
      ],
      "metadata": {
        "id": "7QCDTGKcsuEw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!nohup streamlit run app.py > logs.txt 2>&1 &"
      ],
      "metadata": {
        "id": "BhMaDppUs2qW"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from pyngrok import ngrok\n",
        "\n",
        "ngrok.set_auth_token(\"...\")\n",
        "\n",
        "public_url = ngrok.connect(8501)\n",
        "\n",
        "print(public_url)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fNR_IJMGs5Pn",
        "outputId": "569ed2a4-eeb5-4a9b-c007-db8576437653"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "NgrokTunnel: \"https://petticoat-colonial-vertical.ngrok-free.dev\" -> \"http://localhost:8501\"\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import files\n",
        "files.download(\"app.py\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 17
        },
        "id": "WHkYvSRE7_S_",
        "outputId": "aaa361c0-f966-4627-df67-be43c6463f84"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "\n",
              "    async function download(id, filename, size) {\n",
              "      if (!google.colab.kernel.accessAllowed) {\n",
              "        return;\n",
              "      }\n",
              "      const div = document.createElement('div');\n",
              "      const label = document.createElement('label');\n",
              "      label.textContent = `Downloading \"${filename}\": `;\n",
              "      div.appendChild(label);\n",
              "      const progress = document.createElement('progress');\n",
              "      progress.max = size;\n",
              "      div.appendChild(progress);\n",
              "      document.body.appendChild(div);\n",
              "\n",
              "      const buffers = [];\n",
              "      let downloaded = 0;\n",
              "\n",
              "      const channel = await google.colab.kernel.comms.open(id);\n",
              "      // Send a message to notify the kernel that we're ready.\n",
              "      channel.send({})\n",
              "\n",
              "      for await (const message of channel.messages) {\n",
              "        // Send a message to notify the kernel that we're ready.\n",
              "        channel.send({})\n",
              "        if (message.buffers) {\n",
              "          for (const buffer of message.buffers) {\n",
              "            buffers.push(buffer);\n",
              "            downloaded += buffer.byteLength;\n",
              "            progress.value = downloaded;\n",
              "          }\n",
              "        }\n",
              "      }\n",
              "      const blob = new Blob(buffers, {type: 'application/binary'});\n",
              "      const a = document.createElement('a');\n",
              "      a.href = window.URL.createObjectURL(blob);\n",
              "      a.download = filename;\n",
              "      div.appendChild(a);\n",
              "      a.click();\n",
              "      div.remove();\n",
              "    }\n",
              "  "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "download(\"download_bf767888-ea93-456c-9db3-08ca5237882e\", \"app.py\", 1145)"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "YPvzHqqj8Ab1"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
