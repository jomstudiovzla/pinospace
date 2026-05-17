import base64
import os

with open("../Logo pino/Logo pino.png", "rb") as f:
    logo = base64.b64encode(f.read()).decode()
with open("../qr page/QR_LandingPage.png", "rb") as f:
    qr = base64.b64encode(f.read()).decode()

html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flyer Pino Espace Verts</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --cream: #f2ede3;
            --sage-light: #b8c9a8;
            --sage: #8fa07e;
            --olive: #6b7a5a;
            --olive-dark: #4e5c40;
            --text: #2c2c2a;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            background: #222;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            font-family: 'Inter', sans-serif;
            margin: 0;
        }}
        /* Wrapper for scaling to fit screen without losing resolution */
        .wrapper {{
            width: 1080px;
            height: 1920px;
            transform-origin: top center;
            transform: scale(0.45);
        }}
        .flyer {{
            width: 1080px;
            height: 1920px;
            background: var(--cream);
            position: relative;
            overflow: hidden;
            color: var(--text);
            display: flex;
            flex-direction: column;
            align-items: center;
            box-shadow: 0 20px 50px rgba(0,0,0,0.5);
        }}
        /* Decorations */
        .deco-circle {{
            position: absolute;
            top: -200px;
            left: -200px;
            width: 900px;
            height: 900px;
            background: radial-gradient(circle, rgba(184,201,168,0.7) 0%, rgba(242,237,227,0) 70%);
            border-radius: 50%;
            z-index: 1;
        }}
        .deco-wave {{
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 500px;
            z-index: 1;
        }}
        
        .content {{
            position: relative;
            z-index: 10;
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100%;
            height: 100%;
            padding: 100px 80px 80px 80px;
        }}
        .logo {{
            width: 320px;
            height: auto;
            margin-bottom: 30px;
            filter: drop-shadow(0 10px 20px rgba(78,92,64,0.2));
        }}
        h1 {{
            font-family: 'Cormorant Garamond', serif;
            font-size: 110px;
            font-weight: 500;
            color: var(--olive-dark);
            text-align: center;
            line-height: 1;
            margin-bottom: 20px;
        }}
        .subtitle {{
            font-family: 'Cormorant Garamond', serif;
            font-size: 45px;
            font-style: italic;
            color: var(--olive);
            text-align: center;
            margin-bottom: 70px;
            max-width: 80%;
            line-height: 1.2;
        }}
        
        /* Offer Banner */
        .offer-banner {{
            background: var(--olive);
            color: var(--cream);
            width: 110%;
            padding: 50px 0;
            text-align: center;
            transform: rotate(-3deg);
            box-shadow: 0 15px 40px rgba(78,92,64,0.3);
            margin-bottom: 90px;
            position: relative;
            z-index: 20;
        }}
        .offer-text {{
            font-size: 75px;
            font-weight: 600;
            transform: rotate(3deg);
            letter-spacing: 2px;
        }}
        .offer-sub {{
            font-size: 40px;
            font-weight: 400;
            transform: rotate(3deg);
            opacity: 0.9;
            margin-top: 15px;
            font-family: 'Cormorant Garamond', serif;
            font-style: italic;
        }}

        /* Services */
        .services {{
            display: flex;
            flex-direction: column;
            gap: 35px;
            width: 100%;
            padding: 0 60px;
            margin-bottom: auto;
        }}
        .service-item {{
            display: flex;
            align-items: center;
            font-size: 45px;
            color: var(--text);
            background: rgba(253, 250, 244, 0.6);
            padding: 30px 40px;
            border-radius: 20px;
            border: 2px solid rgba(143,160,126,0.3);
            backdrop-filter: blur(10px);
            box-shadow: 0 10px 20px rgba(78,92,64,0.05);
        }}
        .service-icon {{
            color: var(--sage);
            margin-right: 35px;
            font-size: 55px;
        }}

        /* Footer */
        .footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
            background: rgba(253, 250, 244, 0.85);
            backdrop-filter: blur(15px);
            border-radius: 40px;
            padding: 60px;
            border: 1px solid rgba(143,160,126,0.3);
            box-shadow: 0 -10px 40px rgba(78,92,64,0.1);
        }}
        .contact-info {{
            display: flex;
            flex-direction: column;
            gap: 35px;
        }}
        .contact-item {{
            display: flex;
            align-items: center;
            font-size: 40px;
            font-weight: 500;
            color: var(--olive-dark);
        }}
        .contact-icon {{
            width: 65px;
            height: 65px;
            background: var(--sage-light);
            border-radius: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 25px;
            color: var(--olive-dark);
        }}
        .contact-icon svg {{ width: 35px; height: 35px; }}
        .qr-box {{
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 20px;
        }}
        .qr-img {{
            width: 280px;
            height: 280px;
            border-radius: 25px;
            box-shadow: 0 15px 30px rgba(78,92,64,0.2);
            border: 4px solid var(--olive);
        }}
        .qr-text {{
            font-size: 32px;
            font-weight: 600;
            color: var(--olive);
            text-transform: uppercase;
            letter-spacing: 3px;
        }}
        
        @media (max-height: 1000px) {{
            .wrapper {{ transform: scale(0.4); }}
        }}
        @media (max-height: 800px) {{
            .wrapper {{ transform: scale(0.35); }}
        }}
    </style>
</head>
<body>
    <div class="wrapper">
        <div class="flyer">
            <div class="deco-circle"></div>
            <svg class="deco-wave" viewBox="0 0 1440 320" preserveAspectRatio="none" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M0,160 C320,300, 420,0, 740,160 C1060,320, 1440,100, 1440,160 L1440,320 L0,320 Z" fill="#b8c9a8" opacity="0.4"/>
                <path d="M0,220 C280,100, 600,280, 900,180 C1200,80, 1440,240, 1440,240 L1440,320 L0,320 Z" fill="#8fa07e" opacity="0.3"/>
            </svg>

            <div class="content">
                <img class="logo" src="data:image/png;base64,{logo}" alt="Logo">
                
                <h1>Pino Espace Verts</h1>
                <div class="subtitle">Entretien et Aménagement d'Espaces Verts</div>

                <div class="offer-banner">
                    <div class="offer-text">-20% DE RÉDUCTION</div>
                    <div class="offer-sub">Sur votre première prestation</div>
                </div>

                <div class="services">
                    <div class="service-item">
                        <span class="service-icon">✦</span>
                        Tonte de pelouse & Débroussaillage
                    </div>
                    <div class="service-item">
                        <span class="service-icon">✦</span>
                        Taille de haies et d'arbustes
                    </div>
                    <div class="service-item">
                        <span class="service-icon">✦</span>
                        Nettoyage & Entretien de jardins
                    </div>
                    <div class="service-item">
                        <span class="service-icon">✦</span>
                        Aménagement paysager sur mesure
                    </div>
                </div>

                <div class="footer">
                    <div class="contact-info">
                        <div class="contact-item">
                            <div class="contact-icon">
                                <svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
                            </div>
                            +33 6 51 59 40 34
                        </div>
                        <div class="contact-item">
                            <div class="contact-icon">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M2 7l10 7 10-7"/></svg>
                            </div>
                            pino.espacesverts@gmail.com
                        </div>
                        <div class="contact-item">
                            <div class="contact-icon">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
                            </div>
                            @pino.espacesverts
                        </div>
                    </div>
                    <div class="qr-box">
                        <img class="qr-img" src="data:image/png;base64,{qr}" alt="QR Code">
                        <div class="qr-text">Scannez-moi</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

os.makedirs("../flyer pino", exist_ok=True)
with open("../flyer pino/flyer_9_16.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Flyer HTML created successfully at ../flyer pino/flyer_9_16.html")
