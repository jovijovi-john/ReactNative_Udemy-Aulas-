Expo: https://docs.expo.dev/guides/using-firebase/

CLI: https://rnfirebase.io/

    npm install firebase@^8.8.1

    cria uma pasta src e dentro dela um arquivo FirebaseConection.js

    dentro desse arquivo:

        ```javascript
        import firebase from 'firebase';
        import "firebase/database";

        let firebaseConfig = {
            ...
        };
        
        // Initialize Firebase

        if (!firebase.apps.length) { // Isso aqui é pra não abrir duas conexões juntas, pois isso gera um erro
            firebase.initializeApp(firebaseConfig);
        }
        export default firebase;

        ```

    Um problema que tive e isso resolveu: 
        https://stackoverflow.com/questions/34969858/react-native-module-appregistry-is-not-a-registered-callable-module

