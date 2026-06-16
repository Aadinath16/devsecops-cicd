document.addEventListener('DOMContentLoaded', () => {
    const itemsContainer = document.getElementById('itemsContainer');
    const toolForm = document.getElementById('toolForm');
    const refreshBtn = document.getElementById('refreshBtn');

    // Function to fetch and display items dynamically
    async function loadItems() {
        try {
            const response = await fetch('/api/items');
            const result = await response.json();
            
            if (result.status === 'success') {
                displayItems(result.data);
            }
        } catch (error) {
            itemsContainer.innerHTML = `<p class="text-red-400">Error loading tools from backend.</p>`;
        }
    }

    // Render items into the DOM
    function displayItems(items) {
        if (items.length === 0) {
            itemsContainer.innerHTML = '<p class="text-gray-500">No tools configured yet.</p>';
            return;
        }

        itemsContainer.innerHTML = items.map(item => {
            const statusColor = item.status === 'Active' ? 'text-green-400 bg-green-950 border-green-800' : 
                                item.status === 'Pending' ? 'text-yellow-400 bg-yellow-950 border-yellow-800' : 
                                'text-gray-400 bg-gray-900 border-gray-700';
            return `
                <div class="flex justify-between items-center bg-gray-750 p-4 rounded border border-gray-700 hover:border-gray-600 transition">
                    <div>
                        <span class="text-xs text-gray-500 font-mono">ID: ${item.id}</span>
                        <h3 class="text-lg font-medium text-white">${item.name}</h3>
                    </div>
                    <span class="px-3 py-1 rounded-full text-xs font-semibold border ${statusColor}">
                        ${item.status}
                    </span>
                </div>
            `;
        }).join('');
    }

    // Handle Form Submission asynchronously
    toolForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const name = document.getElementById('toolName').value;
        const status = document.getElementById('toolStatus').value;

        try {
            const response = await fetch('/api/items', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ name, status })
            });

            if (response.ok) {
                toolForm.reset();
                loadItems(); // Refresh the list instantly
            }
        } catch (error) {
            alert('Failed to save the tool.');
        }
    });

    refreshBtn.addEventListener('click', loadItems);

    // Initial Load
    loadItems();
});