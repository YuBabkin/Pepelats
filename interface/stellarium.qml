import QtQuick 2.6
import QtQuick.Controls 2.0
import QtQuick.Controls 1.4
import QtQuick.Window 2.0


ApplicationWindow {

    Item {
        id: mainScope
        property var background: "#024E68"
        property var foreground: "#91e0ec"
        property var highlight: "#afedf6"
        property var shadow: "#7eabb1"
        property var textcolor: foreground
        property var fontfamily: "Helvetica"
        property var fontsize: 24
        property var radius: 20
    }

    id: mainwin
    visible: true
    width: 1940; height: 1080;

     menuBar: MenuBar {
         Menu {
             title: "File"
             MenuItem {
                 text: "Open"
             }
             MenuItem {text: "Close" }
         }
    }

    Grid{
        x: 4; anchors.right: mainwin.right; anchors.bottomMargin: 4
        rows: 3; columns: 1; spacing: 3;
        Button {
            enabled: false
        }
    }
}
