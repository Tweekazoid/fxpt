from PySide import QtCore, QtGui

from fxpt.fx_prefsaver import PrefSaver, Serializers
from fxpt.fx_textureManager.CopyMoveDialogUI import Ui_Dialog

from fxpt.fx_textureManager.CopyMoveInfo import CopyMoveInfo

OPT_VAR_NAME_COPY_MOVE_DLG = 'fx_textureManager_copMoveDlg_prefs'


class CopyMoveDialog(QtGui.QDialog):

    def __init__(self, parent):
        super(CopyMoveDialog, self).__init__(parent=parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.lastBrowsedDirTarget = ''
        self.lastBrowsedDirSource = ''

        self.ui_initSettings()
        self.ui_loadSettings()

        self.validateUi()

    # noinspection PyAttributeOutsideInit
    def ui_initSettings(self):
        self.prefSaver = PrefSaver.PrefSaver(Serializers.SerializerOptVar(OPT_VAR_NAME_COPY_MOVE_DLG))

        self.prefSaver.addControl(self, PrefSaver.UIType.PYSIDEWindow, (200, 200, 800, 350))
        self.prefSaver.addControl(self.ui.uiLED_targetRoot, PrefSaver.UIType.PYSIDELineEdit, '')
        self.prefSaver.addControl(self.ui.uiCHK_deleteSources, PrefSaver.UIType.PYSIDECheckBox, False)
        self.prefSaver.addControl(self.ui.uiGRP_folderStructure, PrefSaver.UIType.PYSIDEGroupBox, False)
        self.prefSaver.addControl(self.ui.uiLED_sourceRoot, PrefSaver.UIType.PYSIDELineEdit, '')
        self.prefSaver.addControl(self.ui.uiGRP_addTextures, PrefSaver.UIType.PYSIDEGroupBox, False)
        self.prefSaver.addControl(self.ui.uiLED_texSuffixes, PrefSaver.UIType.PYSIDELineEdit, '_nm, _spec, _hdetm, _em')
        self.prefSaver.addControl(self.ui.uiCHK_retarget, PrefSaver.UIType.PYSIDECheckBox, False)
        self.prefSaver.addControl(self.ui.uiCHK_forceRetarget, PrefSaver.UIType.PYSIDECheckBox, False)

        self.prefSaver.addVariable('retargetDlg_lastBrowsedDirTarget', self.getLastBrowsedDirTarget, self.setLastBrowsedDirTarget, '')
        self.prefSaver.addVariable('retargetDlg_lastBrowsedDirSource', self.getLastBrowsedDirSource, self.setLastBrowsedDirSource, '')

    def ui_loadSettings(self):
        self.prefSaver.loadPrefs()

    def ui_saveSettings(self):
        self.prefSaver.savePrefs()

    def setLastBrowsedDirTarget(self, path):
        self.lastBrowsedDirTarget = path

    def getLastBrowsedDirTarget(self):
        return self.lastBrowsedDirTarget

    def setLastBrowsedDirSource(self, path):
        self.lastBrowsedDirSource = path

    def getLastBrowsedDirSource(self):
        return self.lastBrowsedDirSource

    def getTargetRoot(self):
        return self.ui.uiLED_targetRoot.getPath()

    def setTargetRoot(self, path):
        self.ui.uiLED_targetRoot.setPath(path)

    def getSourceRoot(self):
        return self.ui.uiLED_sourceRoot.getPath()

    def setSourceRoot(self, path):
        self.ui.uiLED_sourceRoot.setPath(path)

    def getDelSrc(self):
        return self.ui.uiCHK_deleteSources.checkState() == QtCore.Qt.Checked

    def getCopyFolderStruct(self):
        return self.ui.uiGRP_folderStructure.isChecked()

    def getCopyAdd(self):
        return self.ui.uiGRP_addTextures.isChecked()

    def getAddSuffixes(self):
        return str(self.ui.uiLED_texSuffixes.text())

    def getRetarget(self):
        return self.ui.uiCHK_retarget.checkState() == QtCore.Qt.Checked

    def getForceRetarget(self):
        return self.ui.uiCHK_forceRetarget.checkState() == QtCore.Qt.Checked

    def validateUi(self):
        targetRootExists = self.ui.uiLED_targetRoot.pathExists()
        self.ui.uiBTN_ok.setEnabled(targetRootExists)
        if targetRootExists:
            self.setStatusText('')
        else:
            self.setStatusText('Target root directory does not exists.')
            return

        if self.getCopyFolderStruct():
            sourceRootExists = self.ui.uiLED_sourceRoot.pathExists()
            self.ui.uiBTN_ok.setEnabled(sourceRootExists)
            if sourceRootExists:
                self.setStatusText('')
            else:
                self.setStatusText('Original source root directory does not exists.')
                return


    def setStatusText(self, text):
        self.ui.uiLBL_status.setText(text)

    def getDialogResult(self):
        res = CopyMoveInfo(
            targetRoot=self.getTargetRoot(),
            delSrc=self.getDelSrc(),
            copyFolderStruct=self.getCopyFolderStruct(),
            sourceRoot=self.getSourceRoot(),
            copyAdd=self.getCopyAdd(),
            addSuffixes=self.getAddSuffixes(),
            retarget=self.getRetarget(),
            forceRetarget=self.getForceRetarget()
        )
        return res

    def onBrowseTargetClicked(self):
        # noinspection PyCallByClass
        dialogResult = QtGui.QFileDialog.getExistingDirectory(
            self,
            'Select Target Directory',
            self.getLastBrowsedDirTarget()
        )
        if dialogResult:
            self.setTargetRoot(dialogResult)
            self.ui.uiLED_targetRoot.onEditingFinished()
            self.setLastBrowsedDirTarget(self.getTargetRoot())
            self.validateUi()

    def onBrowseSourceClicked(self):
        # noinspection PyCallByClass
        dialogResult = QtGui.QFileDialog.getExistingDirectory(
            self,
            'Select Original Root Directory',
            self.getLastBrowsedDirSource()
        )
        if dialogResult:
            self.setSourceRoot(dialogResult)
            self.ui.uiLED_sourceRoot.onEditingFinished()
            self.setLastBrowsedDirSource(self.getSourceRoot())
            self.validateUi()

    def onRetargetClicked(self):
        self.ui.uiCHK_forceRetarget.setEnabled(self.ui.uiCHK_retarget.checkState() == QtCore.Qt.Checked)

    def onValidateUiNeeded(self):
        self.validateUi()

    def onOkClicked(self):
        self.validateUi()
        if self.ui.uiBTN_ok.isEnabled():
            self.accept()

    # noinspection PyUnusedLocal
    def onDialogFinished(self, status):
        self.ui_saveSettings()