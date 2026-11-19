const socket = new WebSocket('ws://localhost:8000/ws');

const statusEl = document.querySelector('#status');
const messagesEl = document.querySelector('#messages');
const chatForm = document.querySelector('#chat-form');
const usernameInput = document.querySelector('#username-input');
const messageInput = document.querySelector('#message-input');

function formatTime () {
  const now = new Date();
  return now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
}

function appendMessage (text, type, sender) {
  const item = document.createElement('div');
  item.classList.add('message', type);

  const meta = document.createElement('span');
  meta.classList.add('meta');
  meta.textContent = sender ? `${sender} • ${formatTime()}` : formatTime();

  const body = document.createElement('span');
  body.textContent = text;

  item.appendChild(meta);
  item.appendChild(body);
  messagesEl.appendChild(item);
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

socket.onopen = () => {
  statusEl.textContent = 'Connected';
  statusEl.classList.remove('disconnected');
  statusEl.classList.add('connected');
  appendMessage('Connected to WebSocket server.', 'system', 'System');
};

socket.onmessage = (event) => {
  appendMessage(event.data, 'received', 'Server');
};

socket.onclose = () => {
  statusEl.textContent = 'Disconnected';
  statusEl.classList.remove('connected');
  statusEl.classList.add('disconnected');
  appendMessage('Connection closed.', 'system', 'System');
};

socket.onerror = () => {
  appendMessage('WebSocket connection error.', 'system', 'System');
};

chatForm.addEventListener('submit', (event) => {
  event.preventDefault();
  const rawText = messageInput.value;
  if (!rawText.trim()) {
    return;
  }
  if (socket.readyState !== WebSocket.OPEN) {
    appendMessage('Socket is not connected.', 'system', 'System');
    return;
  }

  const user = usernameInput.value.trim() || 'You';
  const payload = usernameInput.value.trim() ? `${usernameInput.value.trim()}: ${rawText}` : rawText;

  socket.send(payload);
  appendMessage(rawText, 'sent', user);
  messageInput.value = '';
  messageInput.focus();
});
