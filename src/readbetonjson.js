// Load the beton photo manifest and build the grid
fetch('betonlijst.json')
  .then(response => response.json())
  .then(data => {
    const gridDiv = document.getElementById('grid');

    data.forEach(({ file, group, title }) => {
      const src = `img/beton/${file}`;

      const box = document.createElement('div');
      box.className = 'grid-box';

      const link = document.createElement('a');
      link.href = src;
      link.dataset.lightbox = group || 'beton-1';
      link.dataset.title = title || '';

      const img = document.createElement('img');
      img.src = src;
      img.loading = 'lazy';

      link.appendChild(img);
      box.appendChild(link);
      gridDiv.appendChild(box);
    });
  })
  .catch(error => console.error(error));
