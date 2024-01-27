# ought to be rendered as bash scripts.
sudo cp novnc_service.service /etc/systemd/system/novnc_service.service
sudo systemctl daemon-reload
sudo systemctl kill novnc_service
sudo systemctl start novnc_service
sudo systemctl enable novnc_service 