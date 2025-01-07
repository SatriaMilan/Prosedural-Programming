function segitigaSamaKaki(tinggi) {
    for (let i = 1; i <= tinggi; i++) {
        let spasi = " ".repeat(tinggi - i);
        let bintang = "*".repeat(2 * i - 1);
        console.log(spasi + bintang);
    }
}

function segitigaSamaKakiTerbalik(tinggi) {
    for (let i = tinggi; i >= 1; i--) {
        let spasi = " ".repeat(tinggi - i);
        let bintang = "*".repeat(2 * i - 1);
        console.log(spasi + bintang);
    }
}

function segitigaSikuSiku(tinggi) {
    for (let i = 1; i <= tinggi; i++) {
        console.log("*".repeat(i));
    }
}

function segitigaSikuSikuTerbalik(tinggi) {
    for (let i = tinggi; i >= 1; i--) {
        console.log("*".repeat(i));
    }
}

function main() {
    while (true) {
        console.log("Menu:");
        console.log("1. Sama Kaki");
        console.log("2. Sama Kaki Terbalik");
        console.log("3. Siku Siku");
        console.log("4. Siku Siku Terbalik");
        console.log("0. Keluar");

        let choice = prompt("Masukkan pilihan Anda: ");

        if (choice === "1") {
            let tinggi = parseInt(prompt("Masukkan tinggi segitiga sama kaki: "));
            segitigaSamaKaki(tinggi);
        } else if (choice === "2") {
            let tinggi = parseInt(prompt("Masukkan tinggi segitiga sama kaki terbalik: "));
            segitigaSamaKakiTerbalik(tinggi);
        } else if (choice === "3") {
            let tinggi = parseInt(prompt("Masukkan tinggi segitiga siku-siku: "));
            segitigaSikuSiku(tinggi);
        } else if (choice === "4") {
            let tinggi = parseInt(prompt("Masukkan tinggi segitiga siku-siku terbalik: "));
            segitigaSikuSikuTerbalik(tinggi);
        } else if (choice === "0") {
            console.log("Keluar dari program");
            break;
        } else {
            console.log("Pilihan tidak valid");
        }
    }
}

main();
