
const messages = Array.from({ length: 50 }, (_, i) => ({
    username: `用户${i + 1}`,
    date: `2025-01-${(i % 31) + 1}`,
    content: `这是第 ${i + 1} 条留言。这是一段比较长的内容，用于测试折叠和展开功能。`
}));
const pageSize = 10;
let currentPage = 1;

function renderMessages() {
    const board = document.getElementById('messageBoard');
    board.innerHTML = '';
    const start = (currentPage - 1) * pageSize;
    const end = Math.min(start + pageSize, messages.length);

    for (let i = start; i < end; i++) {
        const message = document.createElement('div');
        message.className = 'message';

        const header = document.createElement('div');
        header.className = 'message-header';
        header.innerHTML = `<span>${messages[i].username}</span><span>${messages[i].date}</span>`;
        message.appendChild(header);

        const content = document.createElement('div');
        content.className = 'message-content';
        content.textContent = messages[i].content;
        message.appendChild(content);

        const button = document.createElement('button');
        button.className = 'toggle-button';
        button.textContent = '展开';
        button.addEventListener('click', () => {
            const isExpanded = message.classList.toggle('expanded');
            button.textContent = isExpanded ? '收起' : '展开';
        });
        message.appendChild(button);

        board.appendChild(message);
    }
}

function renderPagination() {
    const pagination = document.getElementById('pagination');
    pagination.innerHTML = '';
    const totalPages = Math.ceil(messages.length / pageSize);

    const createPageButton = (page) => {
        const button = document.createElement('button');
        button.textContent = page;
        button.disabled = page === currentPage;
        button.addEventListener('click', () => {
            currentPage = page;
            renderMessages();
            renderPagination();
        });
        return button;
    };

    if (totalPages > 4) {
        const buttons = [];
        if (currentPage > 2) {
            buttons.push(createPageButton(1));
            if (currentPage > 3) {
                const dots = document.createElement('span');
                dots.textContent = '...';
                pagination.appendChild(dots);
            }
        }

        const start = Math.max(1, Math.min(currentPage - 1, totalPages - 3));
        const end = Math.min(totalPages, start + 3);

        for (let i = start; i <= end; i++) {
            pagination.appendChild(createPageButton(i));
        }

        if (currentPage < totalPages - 1) {
            if (currentPage < totalPages - 2) {
                const dots = document.createElement('span');
                dots.textContent = '...';
                pagination.appendChild(dots);
            }
            pagination.appendChild(createPageButton(totalPages));
        }
    } else {
        for (let i = 1; i <= totalPages; i++) {
            pagination.appendChild(createPageButton(i));
        }
    }
}

renderMessages();
renderPagination();
