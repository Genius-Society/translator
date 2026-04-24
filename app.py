import json
import requests
import gradio as gr
from utils import API_TRANS, KEY_TRANS, EN_US

ZH2EN = {
    "输入文本区域": "Input text area",
    "在这里输入文本...": "Type the text here...",
    "模式": "Mode",
    "翻译结果": "Translation results",
    "状态栏": "Status",
    "翻译器": "Translator",
}


def _L(zh_txt: str):
    return ZH2EN[zh_txt] if EN_US else zh_txt


def infer(source, direction):
    status = "Success"
    result = None
    try:
        if not source or not direction:
            raise ValueError("请输入有效文本!")

        response = requests.request(
            "POST",
            API_TRANS,
            data=json.dumps(
                {
                    "source": source,
                    "trans_type": direction,
                    "request_id": "demo",
                    "detect": True,
                }
            ),
            headers={
                "content-type": "application/json",
                "x-authorization": f"token {KEY_TRANS}",
            },
        )

        result = json.loads(response.text)["target"]

    except Exception as e:
        status = f"{e}"

    return status, result


if __name__ == "__main__":
    gr.Interface(
        fn=infer,
        inputs=[
            gr.TextArea(label=_L("输入文本区域"), placeholder=_L("在这里输入文本...")),
            gr.Textbox(label=_L("模式"), value="auto2en"),
        ],
        outputs=[
            gr.Textbox(label=_L("状态栏"), buttons=["copy"]),
            gr.TextArea(label=_L("翻译结果"), buttons=["fullscreen", "copy"]),
        ],
        flagging_mode="never",
        examples=[
            ["这是最好的翻译服务。", "auto2ja"],
            ["これは最高の翻訳サービスです。", "auto2en"],
            ["This is the best translation service.", "auto2zh"],
        ],
        cache_examples=False,
        title=_L("翻译器"),
    ).launch(css="#gradio-share-link-button-0 { display: none; }")
