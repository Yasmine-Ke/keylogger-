# keylogger-


#  Rapport : Création et Lancement d'un Keylogger en Arrière-plan 

---

##  Objectif
Ce rapport vise à expliquer la **création d'un keylogger basique en Python** et son lancement en arrière-plan sur un système Linux en utilisant la commande `nohup`. L'objectif est de permettre au keylogger de rester actif même après la fermeture du terminal, garantissant ainsi la capture continue des frappes.

---

##  **1. Introduction**

Un keylogger est un programme qui enregistre les frappes effectuées par l'utilisateur sur un clavier. Dans ce rapport, nous allons aborder :

1. **La création d'un keylogger simple avec Python.**
2. **Son lancement en arrière-plan en utilisant `nohup`.**

---

##  **2. Création du Keylogger**

### 📄 **2.1. Code Source**

Pour créer un keylogger simple, nous utilisons le module `pynput` qui permet de capturer les frappes (keypress) d'un clavier.


---

##  **3. Lancer le Keylogger en Arrière-plan avec `nohup`**

La commande `nohup` est utilisée pour permettre à un processus de s'exécuter en arrière-plan même après la fermeture du terminal. C'est la meilleure pratique pour que le processus reste actif.

###  **Commandes**

1. **Exécution avec `nohup` :**
   ```bash
   nohup python3 key.py &
   ```

   - **`nohup` :** Permet au processus de continuer à s'exécuter même après la déconnexion ou la fermeture du terminal.
   - **`&` :** Permet de lancer le processus en arrière-plan.

---

###  **Vérification du processus**

Pour vérifier que le keylogger est bien en cours d'exécution après la commande :

```bash
ps aux | grep keylogger.py
```

---

###  **Pour arrêter le processus**
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



📌 **Fichier clé :**  
- `keyl.py`

📌 **Commandes clés pour le lancement :**
```bash
nohup python3 keylogger.py &
ps aux | grep keylogger.py
```

---

**Bonne pratique :** Pour des tests ou de la recherche, configurez toujours un environnement virtuel sécurisé pour éviter tout risque.

---

