
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('predictionForm');
    const imageInput = document.getElementById('image');
    const previewImage = document.getElementById('previewImage');
    const resultSection = document.getElementById('resultSection');
    const resultContent = document.getElementById('resultContent');

    // Prévisualisation de l'image
    imageInput.addEventListener('change', function(e) {
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                previewImage.src = e.target.result;
                previewImage.classList.remove('h-16', 'w-16');
                previewImage.classList.add('max-h-64', 'w-auto');
            };
            reader.readAsDataURL(file);
        }
    });

    // Gestion du drag & drop
    const dropZone = document.querySelector('.border-dashed');

    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        dropZone.addEventListener(eventName, preventDefaults, false);
    });

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    ['dragenter', 'dragover'].forEach(eventName => {
        dropZone.addEventListener(eventName, highlight, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropZone.addEventListener(eventName, unhighlight, false);
    });

    function highlight(e) {
        dropZone.classList.add('border-blue-500', 'bg-blue-50');
    }

    function unhighlight(e) {
        dropZone.classList.remove('border-blue-500', 'bg-blue-50');
    }

    dropZone.addEventListener('drop', handleDrop, false);

    function handleDrop(e) {
        const dt = e.dataTransfer;
        const file = dt.files[0];
        imageInput.files = dt.files;

        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                previewImage.src = e.target.result;
                previewImage.classList.remove('h-16', 'w-16');
                previewImage.classList.add('max-h-64', 'w-auto');
            };
            reader.readAsDataURL(file);
        }
    }

    // Gestion de la soumission du formulaire
    form.addEventListener('submit', async function(e) {
        e.preventDefault();

        // Afficher un loader
        resultContent.innerHTML = `
            <div class="flex justify-center items-center py-8">
                <div class="loading-spinner"></div>
            </div>
        `;
        resultSection.classList.remove('hidden');

        const formData = new FormData(form);

        try {
            const response = await fetch('/predict/', {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            });

            const data = await response.json();

            if (data.success) {
                // Afficher les résultats
                let resultsHTML = '<div class="space-y-4">';

                // Pour chaque modèle
                for (const [model, results] of Object.entries(data.results)) {
                    const isPositive = results.prediction;
                    const confidence = parseFloat(results.confiance);

                    resultsHTML += `
                        <div class="prediction-result ${isPositive ? 'bg-red-50' : 'bg-green-50'} p-4 rounded-lg">
                            <h3 class="font-semibold text-lg mb-2">Modèle ${model.toUpperCase()}</h3>
                            <p class="text-lg mb-2">
                                <span class="font-medium">Résultat :</span> 
                                <span class="${isPositive ? 'text-red-600' : 'text-green-600'}">
                                    ${isPositive ? 'BCC détecté' : 'Pas de BCC'}
                                </span>
                            </p>
                            <div class="mt-2">
                                <div class="flex justify-between mb-1">
                                    <span>Confiance</span>
                                    <span>${results.confiance}</span>
                                </div>
                                <div class="w-full bg-gray-200 rounded-full h-2">
                                    <div class="confidence-bar" style="width: ${results.confiance}"></div>
                                </div>
                            </div>
                        </div>
                    `;
                }

                resultsHTML += '</div>';
                resultContent.innerHTML = resultsHTML;
            } else {
                throw new Error(data.error);
            }
        } catch (error) {
            resultContent.innerHTML = `
                <div class="bg-red-50 text-red-600 p-4 rounded-lg">
                    <p class="font-medium">Une erreur est survenue :</p>
                    <p>${error.message}</p>
                </div>
            `;
        }
    });
});