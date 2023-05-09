const chatOutput = document.getElementById('chat-output');
const inputField = document.getElementById('input-field');
const sendButton = document.getElementById('send-button');

// 调用 chatgpt 模型生成回答
function generateAnswer(inputText) {
    // 调用 chatgpt 接口并返回 Promise 对象
    return fetch('https://api.openai.com/v1/engine/davinci-codex/completions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer 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' // 请替换 YOUR_API_KEY 为你的 OpenAI API Key
        },
        body: JSON.stringify({
            prompt: `Q: ${inputText}\nA: `, // 输入当前的问题
            max_tokens: 1024, // 控制回答长度的最大标记数量
            n: 1, // 控制返回的建议数量
            stop: ['\n'] // 设置 stop words，返回完整句子
        })
    })
        .then(response => response.json())
        .then(data => data.choices[0].text.trim())
        .catch(error => console.error('Error generating answer:', error))
}

// 在聊天框中显示提示信息
function showHint(message) {
    chatOutput.innerHTML += `<div class="hint">${message}</div>`;
    chatOutput.scrollTop = chatOutput.scrollHeight;
}

// 在聊天框中显示回答
function showAnswer(answer) {
    chatOutput.innerHTML += `<div class="answer">${answer}</div>`;
    chatOutput.scrollTop = chatOutput.scrollHeight;
}

// 发送按钮点击事件处理函数
function handleSendButtonClick() {
    const inputText = inputField.value.trim();
    if (inputText) {
        showHint(inputText); // 先显示用户的输入内容
        generateAnswer(inputText)
            .then(answer => showAnswer(answer)) // 显示机器人的回答
            .catch(error => console.error('Error handling send button click:', error));
        inputField.value = ''; // 清空输入框
    }
}

sendButton.addEventListener('click', handleSendButtonClick);
