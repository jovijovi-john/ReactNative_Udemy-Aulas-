O SafeAreaView não faz diferença no android. No ios ele garantirá que todo o conteúdo ficará APÓS a SafeAreaView  e não sobre ela.

Icons:

    docs: https://github.com/oblador/react-native-vector-icons
    npm install react-native-vector-icons

    -> para android: 
        Edit android/app/build.gradle ( NOT android/build.gradle ) and add the following:

            apply from: "../../node_modules/react-native-vector-icons/fonts.gradle"
            To customize the files being copied, add the following instead:

                project.ext.vectoricons = [
                    iconFontNames: [ 'MaterialIcons.ttf', 'EvilIcons.ttf', 'Feather.ttf' ] // Name of the font files you want to copy
                ]

                apply from: "../../node_modules/react-native-vector-icons/fonts.gradle"

    -> para IOS:

        ios/AppTarefas/info.plist

        antes do false:

            <key>UIAppFonts</key>
            <array>
                <string>AntDesign.ttf</string>
                <string>Entypo.ttf</string>
                <string>EvilIcons.ttf</string>
                <string>Feather.ttf</string>
                <string>FontAwesome.ttf</string>
                <string>FontAwesome5_Brands.ttf</string>
                <string>FontAwesome5_Regular.ttf</string>
                <string>FontAwesome5_Solid.ttf</string>
                <string>Foundation.ttf</string>
                <string>Ionicons.ttf</string>
                <string>MaterialIcons.ttf</string>
                <string>MaterialCommunityIcons.ttf</string>
                <string>SimpleLineIcons.ttf</string>
                <string>Octicons.ttf</string>
                <string>Zocial.ttf</string>
                <string>Fontisto.ttf</string>
            </array>

TouchableWithoutFeedback é um botão sem nenhum efeito visual

Precisamos criar o banco de dados que ainda não criamos, um realTimeDatabase. Deixe as configurações de leitura e escrita como true.