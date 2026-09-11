# IONOS-KI

Flask-basierter IONOS-KI-Prototyp mit Login, Registrierung und Chat-API.

## Code-Bereinigung
- Hardcodierter Flask-Secret-Key entfernt.
- Hardcodierter Admin-Benutzer und Klartext-Passwort entfernt.
- Passwortspeicherung auf sichere Hashes umgestellt.
- Doppelter/unreachable Backend-Import am Dateiende entfernt.
- Konfiguration über `SECRET_KEY`, `DATABASE_URL` und `PORT`.

Die vorhandenen Frontend-, AI-, Memory-, Render- und Deployment-Dateien bleiben erhalten und werden separat geprüft.
