# UI/UX Workflow

Framework mandiri untuk menghasilkan frontend web/webview yang sesuai konteks, konsisten, dan dapat diverifikasi melalui Codex atau Claude Code. Versi paket: **0.2.0**.

Paket menggabungkan rules pemicu singkat, enam skills yang dimuat sesuai fase, dan artefak desain per proyek. Tidak bergantung pada Super Compound, framework frontend, layanan image tertentu, plugin, atau server tambahan.

## Instalasi

Butuh **Python 3.10+**. Jalankan perintah dari direktori paket ini. Tidak ada dependency pip dan tidak perlu hak administrator atau symlink. Pilih scope dan platform secara eksplisit.

**Per repository**, contoh Windows:

```powershell
python scripts/install.py --scope project --platform both --project-dir "D:\Projects\aplikasi-saya" --dry-run
python scripts/install.py --scope project --platform both --project-dir "D:\Projects\aplikasi-saya"
```

**Global**, tersedia pada semua proyek pengguna:

```sh
python scripts/install.py --scope user --platform both --dry-run
python scripts/install.py --scope user --platform both
```

Gunakan `--platform codex` atau `--platform claude` jika hanya membutuhkan satu platform. Untuk proyek aktif, `--project-dir` boleh dihilangkan apabila working directory memang root proyek target. Di macOS/Linux gunakan path proyek setempat dan `python3` jika itu nama interpreter yang tersedia.

| Scope | Codex | Claude Code |
| --- | --- | --- |
| Proyek | `.agents/skills/`, rules di `AGENTS.md` | `.claude/skills/`, `CLAUDE.md` mengimpor `@AGENTS.md` |
| Global | `~/.agents/skills/`, rules di `~/.codex/AGENTS.md` | `~/.claude/skills/`, rules di `~/.claude/CLAUDE.md` |

Untuk rules Codex global, installer menghormati `CODEX_HOME` bila disetel; lokasi skill global tetap mengikuti direktori discovery Codex. Semua enam skills dipasang bersama agar referensi antar-fase tetap valid. Metadata `agents/openai.yaml` hanya disertakan untuk Codex.

Mulai sesi baru setelah pemasangan agar discovery/rules dimuat. Pada sesi awal proyek, router memeriksa konteks dan membuat dokumentasi hanya ketika dibutuhkan; installer tidak membuat dokumen desain kosong.

### Update dan konflik

Jalankan installer dari versi paket baru dengan argumen yang sama. Pemasangan ulang identik tidak mengubah file. Installer mencatat versi dan kepemilikan dalam `.ui-ux-workflow/install.json` di root proyek atau home pengguna. Pertahankan manifest ini bersama file hasil instalasi ketika memindahkan atau menyalin proyek; manifest bukan dokumen desain.

Pada instalasi proyek yang memakai kedua platform, update versi harus menggunakan `--platform both` karena Claude dan Codex berbagi rules `AGENTS.md`. Update global masing-masing platform tetap dapat dilakukan terpisah karena rules globalnya terpisah.

Instruksi di luar blok `ui-ux-workflow` tetap dipertahankan. Installer memeriksa semua tujuan sebelum menulis. Jika ada file skill atau blok rules yang diedit lokal, file yang sudah ada tetapi tidak dimiliki installer, atau lokasi yang tidak aman, installer berhenti dengan path konflik. `--dry-run` juga melaporkan konflik tanpa menulis apa pun.

Untuk menyelesaikan konflik, salin perubahan lokal ke tempat yang aman, bandingkan dengan versi paket yang sebelumnya dipasang, dan pulihkan hanya file/blok milik paket yang ingin diperbarui. Simpan aturan proyek tambahan di luar blok terkelola. Jalankan dry-run kembali sebelum update. Tidak ada `--force` yang menghapus modifikasi diam-diam. Kegagalan I/O dilaporkan sebagai kegagalan; preflight konflik bukan janji transaksi filesystem jika proses terputus.

Jika memilih instalasi proyek di atas instalasi global, pastikan versi aktif yang dilaporkan agent sesuai versi proyek. Kemampuan discovery/precedence bergantung pada host; hindari mempertahankan dua versi tanpa kebutuhan. Simpan sumber versi paket yang dipakai agar update dapat ditelusuri.

## Pemakaian

Setelah terpasang, gunakan bahasa biasa:

> Buat dashboard operasional untuk supervisor gudang. Backend sudah ada. Gunakan referensi ini untuk kepadatan informasi, lalu bantu sampai implementasinya terverifikasi.

> Rapikan checkbox Select Message di sidepanel ini tanpa mengubah business logic.

> Samakan perilaku review dan submit Open Ticket dan Close Ticket, tetapi pertahankan perbedaan permission dan payload.

Jika pemicu otomatis tidak memilih framework, gunakan **`$ui-ux` di Codex** atau **`/ui-ux` di Claude Code**, diikuti instruksi. Agent juga dapat membaca `SKILL.md` yang terpasang secara langsung jika host tidak menyediakan mekanisme invocation tersebut. Skills fase tetap tersedia untuk pekerjaan spesifik dan memeriksa prasyaratnya sendiri.

| Skill | Hasil |
| --- | --- |
| `ui-ux` | Discovery, interview seperlunya, pemilihan jalur, dan resume |
| `ui-ux-style` | Image arah visual dan keputusan styling |
| `ui-ux-prototype` | HTML interaktif dengan fixtures terisolasi |
| `ui-ux-plan` | Plan produksi dengan acceptance criteria dan dependensi |
| `ui-ux-build` | Implementasi per tugas pengguna dan bukti hasil |
| `ui-ux-review` | Pemeriksaan produksi, gap, dan handoff review |

### Routing model dan effort

`ui-ux` memilih profil model dan effort sesuai scope, risiko, serta kemampuan host sebelum meneruskan fase. Invocation langsung pada skill fase menjalankan pemeriksaan yang sama. Pilihan diselesaikan menjadi model konkret yang tersedia; paket tidak mengunci model terbaru atau harga provider.

| Skill | Waktu pemilihan |
| --- | --- |
| `ui-ux-build` | Sebelum perubahan production code |
| `ui-ux-review` | Sebelum proses review, termasuk reviewer yang didelegasikan |
| `ui-ux-style` | Tepat sebelum menghasilkan image atau visual artifact |
| `ui-ux-prototype` | Tepat sebelum menghasilkan mockup HTML interaktif |
| `ui-ux-plan` | Sebelum menyusun plan; default model reasoning yang sesuai dengan effort `high`, atau `xhigh` untuk pekerjaan yang lebih kompleks bila didukung |

Sebelum fase berjalan, tampilkan tujuh hal: **skill dan fase, scope, model rekomendasi, effort rekomendasi, alasan, alternatif lebih hemat bila tersedia, serta estimasi biaya/waktu bila dapat diketahui**. Jika estimasi tidak tersedia, nyatakan hal itu; angka tidak boleh direka. Untuk visual, bedakan model reasoning dari generator image dan setting yang benar-benar dapat dikendalikan tool.

Minta approval bila pilihan berpotensi memberi peningkatan biaya, waktu, atau kualitas output yang signifikan dalam konteks task. Tidak ada ambang angka universal. Reuse approval yang masih berlaku bila skill/fase, scope, model, effort dan artefak yang dituju tidak berubah. Penolakan menghentikan fase tersebut dan diikuti penawaran alternatif lebih rendah; alternatif tidak dijalankan diam-diam.

Catat rekomendasi, scope, approval dan pengaturan efektif dalam `docs/ui-ux/work/<task-id>/model-routing.md`. Rekomendasi bukan bukti bahwa runtime sudah berganti. Jika host tidak menyediakan pergantian otomatis, tunda fase yang bergantung pada pilihan tersebut sampai pengguna mengganti dan mengonfirmasi pengaturan; pekerjaan independen dapat dilanjutkan. Catat konfirmasi pengguna sebagai attestation bila pengaturan aktif tidak dapat diamati dari host. Framework tidak mengubah konfigurasi global untuk memaksakan pilihan.

Approval model hanya mengizinkan eksekusi fase terkait. Approval visual, interaksi, implementasi dan hasil akhir tetap dicatat terpisah. Detail ada di [kebijakan routing](skills/ui-ux/references/model-routing.md) dan [template keputusan](skills/ui-ux/templates/model-routing.md).

## Alur adaptif

```text
Inspect → interview keputusan yang belum jelas → pilih jalur
  UI baru/perubahan material:
    image → approval visual → HTML interaktif → approval interaksi
    → plan → build → review → perbaiki gap → review pengguna
  Perbaikan lokal:
    baseline yang relevan → plan ringkas → perbaikan → pemeriksaan terarah
```

Greenfield/brownfield, kesiapan backend, scope halaman/flow, referensi, dan dampak perubahan dinilai terpisah. Backend-only tidak memicu workflow UI. Request audit atau prototype-only berhenti pada hasil yang diminta.

Untuk UI baru atau perubahan material, default dua arah image yang berbeda secara komposisi, hierarchy atau density. Arahan tunggal yang sudah jelas dapat memakai satu kandidat. Image mengunci maksud visual; HTML mengunci struktur informasi dan interaksi. Keduanya tidak membuktikan integrasi, accessibility, atau performa produksi.

Approval yang masih sesuai tidak diminta ulang. Perubahan material hanya membuka kembali keputusan dan bukti yang terdampak. Perbaikan kecil boleh memakai existing UI sebagai baseline setelah diaudit meskipun proyek belum memiliki arsip approval historis.

Prototipe memakai dummy data realistis, dapat di-reset, dan tidak menghubungi API nyata. Kode eksperimen tidak otomatis masuk produksi. Data mock dapat menjadi hasil akhir untuk scope frontend-only; fitur yang menjanjikan integrasi nyata tetap belum selesai selama hanya memakai mock.

## Artefak proyek

Artefak berada di **root repository target**, bukan di direktori instalasi skill atau parent repository:

```text
docs/ui-ux/
  README.md
  design-system/foundations.md
  work/<task-id>/
    brief.md
    references/
    styling/v001/
    prototype/v001/
    model-routing.md
    approvals.md
    plan.md
    verification/
```

Folder dibuat saat diperlukan. Task kecil dapat menggabungkan brief dan plan. `model-routing.md` menyimpan keputusan eksekusi fase; `approvals.md` menyimpan keputusan desain dan hasil. Revisi approved dipertahankan; revisi baru tidak otomatis approved. Templates ada di masing-masing skill dan contoh pengisian ada di [contoh perbaikan lokal](examples/local-fix.md) serta [contoh fitur terintegrasi](examples/integrated-feature.md).

## Kualitas dan definisi selesai

Anti-slop berarti keputusan yang sesuai pekerjaan pengguna: hierarchy jelas, konten domain yang realistis, density yang tepat, konsistensi, feedback lengkap, responsive container, accessibility, performa dan business rules yang terjaga. Tidak ada larangan gaya universal atau skor kecantikan buatan.

Setiap acceptance criterion memiliki status `unverified`, `verified`, `failed`, atau `blocked`, dengan bukti aktual untuk revisi yang berlaku. Ketidakberlakuan harus memiliki alasan; scope yang dikecualikan tidak dihitung sebagai test lulus. Klaim 100% membutuhkan seluruh kriteria dalam scope terverifikasi. User acceptance dicatat terpisah dari hasil pengujian.

Framework memakai tool yang tersedia. Jika image generation tidak tersedia, image dapat berupa SVG/PNG statis dengan asal yang dijelaskan. Source inspection tidak menggantikan browser interaction. Jika suatu bukti wajib belum bisa diperoleh, agent melanjutkan pekerjaan independen lalu melaporkan langkah yang masih blocked/unverified.

## Pengujian dan referensi

```sh
python -m unittest discover -s tests -v
```

Suite menguji installer menggunakan direktori sementara dan kontrak distribusi skill. Lihat [panduan pengujian](docs/testing.md), [hasil verifikasi 0.2.0](docs/verification/0.2.0/results.md), serta [pemetaan implementasi awal](docs/implementation-plan.md). [Hasil 0.1.0](docs/verification/results.md) adalah evidence historis dan tidak membuktikan routing versi baru. Pengujian keputusan agent adalah sampel perilaku, bukan bukti universal auto-trigger atau kualitas visual semua proyek.

Struktur diadaptasi dari pola engineering modular [AI Hero](https://www.aihero.dev/skills) dan [Matt Pocock Skills](https://github.com/mattpocock/skills), dengan instruksi frontend yang ditulis untuk paket ini. Format mengikuti [Agent Skills](https://agentskills.io/specification); konfigurasi host mengikuti [Codex skills](https://learn.chatgpt.com/docs/build-skills) dan [Claude Code skills](https://code.claude.com/docs/en/skills). Kontrak accessibility menggunakan [WCAG 2.2](https://www.w3.org/WAI/WCAG22/quickref/) dan [ARIA APG](https://www.w3.org/WAI/ARIA/apg/).
