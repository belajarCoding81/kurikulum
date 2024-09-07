document.addEventListener('DOMContentLoaded', function () {
    // Pilih semua elemen filter sidebar admin
    var filterTitles = document.querySelectorAll('.filter-title');
    
    // Loop setiap filter dan tambahkan event listener untuk klik
    filterTitles.forEach(function (title) {
        title.style.cursor = 'pointer';  // Mengubah kursor jadi pointer
        
        // Event untuk toggle (buka/tutup) saat diklik
        title.addEventListener('click', function () {
            var filterSpec = title.nextElementSibling;
            if (filterSpec.style.display === 'none' || filterSpec.style.display === '') {
                filterSpec.style.display = 'block';  // Buka filter jika ditutup
            } else {
                filterSpec.style.display = 'none';  // Tutup filter jika dibuka
            }
        });
    });
});
