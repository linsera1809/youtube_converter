pyinstaller --noconfirm --log-level=WARN \
    --onefile --nowindow \
    --add-data="README:." \
    --add-data="./public/icon.png:img" \
    --add-binary="libfoo.so:lib" \
    --hidden-import=secret1 \
    --hidden-import=secret2 \
    --upx-dir=/usr/local/share/ \
    app.spec