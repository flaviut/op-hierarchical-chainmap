import timeit
from op_hierarchical_chainmap import ChainMap as CChainmap, HierarchicalChainMap as CHierarchicalChainMap
from collections import ChainMap as PChainMap
default_settings = {
    "serial": {
        "port": None,
        "baudrate": None,
        "exclusive": True,
        "lowLatency": False,
        "autoconnect": False,
        "log": False,
        "timeout": {
            "detectionFirst": 10,
            "detectionConsecutive": 2,
            "connection": 10,
            "communication": 30,
            "communicationBusy": 3,
            "temperature": 5,
            "temperatureTargetSet": 2,
            "temperatureAutoreport": 2,
            "sdStatus": 1,
            "sdStatusAutoreport": 1,
            "posAutoreport": 5,
            "resendOk": 0.5,
            "baudrateDetectionPause": 1.0,
            "positionLogWait": 10.0,
        },
        "maxCommunicationTimeouts": {"idle": 2, "printing": 5, "long": 5},
        "maxWritePasses": 5,
        "additionalPorts": [],
        "additionalBaudrates": [],
        "blacklistedPorts": [],
        "blacklistedBaudrates": [],
        "longRunningCommands": ["G4", "G28", "G29", "G30", "G32", "M400", "M226", "M600"],
        "blockedCommands": ["M0", "M1"],
        "ignoredCommands": [],
        "pausingCommands": ["M0", "M1", "M25"],
        "emergencyCommands": ["M112", "M108", "M410"],
        "checksumRequiringCommands": ["M110"],
        "helloCommand": "M110 N0",
        "disconnectOnErrors": True,
        "ignoreErrorsFromFirmware": False,
        "terminalLogSize": 20,
        "lastLineBufferSize": 50,
        "logResends": True,
        "supportResendsWithoutOk": "detect",
        "logPositionOnPause": True,
        "logPositionOnCancel": False,
        "abortHeatupOnCancel": True,
        "waitForStartOnConnect": False,
        "alwaysSendChecksum": False,
        "neverSendChecksum": False,
        "sendChecksumWithUnknownCommands": False,
        "unknownCommandsNeedAck": False,
        "sdRelativePath": False,
        "sdAlwaysAvailable": False,
        "sdLowerCase": False,
        "maxNotSdPrinting": 2,
        "swallowOkAfterResend": True,
        "repetierTargetTemp": False,
        "externalHeatupDetection": True,
        "supportWait": True,
        "ignoreIdenticalResends": False,
        "identicalResendsCountdown": 7,
        "supportFAsCommand": False,
        "firmwareDetection": True,
        "blockWhileDwelling": False,
        "useParityWorkaround": "detect",
        "maxConsecutiveResends": 10,
        "sendM112OnError": True,
        "disableSdPrintingDetection": False,
        "ackMax": 1,
        "sanityCheckTools": True,
        "notifySuppressedCommands": "warn",
        "capabilities": {
            "autoreport_temp": True,
            "autoreport_sdstatus": True,
            "autoreport_pos": True,
            "busy_protocol": True,
            "emergency_parser": True,
            "extended_m20": True,
        },
        "resendRatioThreshold": 10,
        "resendRatioStart": 100,
        # command specific flags
        "triggerOkForM29": True,
    },
    "server": {
        "host": None,
        "port": 5000,
        "firstRun": True,
        "startOnceInSafeMode": False,
        "ignoreIncompleteStartup": False,
        "incompleteStartup": False,
        "seenWizards": {},
        "secretKey": None,
        "heartbeat": 15 * 60,  # 15 min
        "reverseProxy": {
            "prefixHeader": None,
            "schemeHeader": None,
            "hostHeader": None,
            "serverHeader": None,
            "portHeader": None,
            "prefixFallback": None,
            "schemeFallback": None,
            "hostFallback": None,
            "serverFallback": None,
            "portFallback": None,
            "trustedDownstream": [],
        },
        "uploads": {
            "maxSize": 1 * 1024 * 1024 * 1024,  # 1GB
            "nameSuffix": "name",
            "pathSuffix": "path",
        },
        "maxSize": 100 * 1024,  # 100 KB
        "commands": {
            "systemShutdownCommand": None,
            "systemRestartCommand": None,
            "serverRestartCommand": None,
            "localPipCommand": None,
        },
        "onlineCheck": {
            "enabled": None,
            "interval": 15 * 60,  # 15 min
            "host": "1.1.1.1",
            "port": 53,
            "name": "octoprint.org",
        },
        "pluginBlacklist": {
            "enabled": None,
            "url": "https://plugins.octoprint.org/blacklist.json",
            "ttl": 15 * 60,  # 15 min
        },
        "diskspace": {
            "warning": 500 * 1024 * 1024,  # 500 MB
            "critical": 200 * 1024 * 1024,  # 200 MB
        },
        "preemptiveCache": {"exceptions": [], "until": 7},
        "ipCheck": {"enabled": True, "trustedSubnets": []},
        "allowFraming": False,
        "cookies": {"secure": False, "samesite": None},
    },
    "webcam": {
        "webcamEnabled": True,
        "timelapseEnabled": True,
        "stream": None,
        "streamRatio": "16:9",
        "streamTimeout": 5,
        "snapshot": None,
        "snapshotTimeout": 5,
        "snapshotSslValidation": True,
        "ffmpeg": None,
        "ffmpegThreads": 1,
        "ffmpegVideoCodec": "libx264",
        "bitrate": "10000k",
        "watermark": True,
        "flipH": False,
        "flipV": False,
        "rotate90": False,
        "ffmpegCommandline": '{ffmpeg} -r {fps} -i "{input}" -vcodec {videocodec} -threads {threads} -b:v {bitrate} -f {containerformat} -y {filters} "{output}"',
        "timelapse": {
            "type": "off",
            "options": {},
            "postRoll": 0,
            "fps": 25,
        },
        "cleanTmpAfterDays": 7,
        "cacheBuster": False,
    },
    "gcodeAnalysis": {
        "maxExtruders": 10,
        "throttle_normalprio": 0.01,
        "throttle_highprio": 0.0,
        "throttle_lines": 100,
        "runAt": "idle",  # 'never', 'idle', 'always'
        "bedZ": 0.0,
    },
    "feature": {
        "temperatureGraph": True,
        "sdSupport": True,
        "keyboardControl": True,
        "pollWatched": False,
        "modelSizeDetection": True,
        "printStartConfirmation": False,
        "printCancelConfirmation": True,
        "uploadOverwriteConfirmation": True,
        "autoUppercaseBlacklist": ["M117", "M118"],
        "g90InfluencesExtruder": False,
        "enforceReallyUniversalFilenames": False,
    },
    "folder": {
        "uploads": None,
        "timelapse": None,
        "timelapse_tmp": None,
        "logs": None,
        "virtualSd": None,
        "watched": None,
        "plugins": None,
        "slicingProfiles": None,
        "printerProfiles": None,
        "scripts": None,
        "translations": None,
        "generated": None,
        "data": None,
    },
    "temperature": {
        "profiles": [
            {"name": "ABS", "extruder": 210, "bed": 100},
            {"name": "PLA", "extruder": 180, "bed": 60},
        ],
        "cutoff": 30,
        "sendAutomatically": False,
        "sendAutomaticallyAfter": 1,
    },
    "printerProfiles": {"default": None},
    "printerParameters": {"pauseTriggers": [], "defaultExtrusionLength": 5},
    "appearance": {
        "name": "",
        "color": "default",
        "colorTransparent": False,
        "colorIcon": True,
        "defaultLanguage": "_default",
        "showFahrenheitAlso": False,
        "fuzzyTimes": True,
        "closeModalsWithClick": True,
        "showInternalFilename": True,
        "components": {
            "order": {
                "navbar": [
                    "settings",
                    "systemmenu",
                    "plugin_announcements",
                    "plugin_logging_seriallog",
                    "plugin_logging_plugintimingslog",
                    "plugin_pi_support",
                    "login",
                ],
                "sidebar": [
                    "plugin_firmware_check_warning",
                    "plugin_firmware_check_info",
                    "connection",
                    "state",
                    "files",
                ],
                "tab": [
                    "temperature",
                    "control",
                    "plugin_gcodeviewer",
                    "terminal",
                    "timelapse",
                ],
                "settings": [
                    "section_printer",
                    "serial",
                    "printerprofiles",
                    "temperatures",
                    "terminalfilters",
                    "gcodescripts",
                    "section_features",
                    "features",
                    "webcam",
                    "accesscontrol",
                    "plugin_gcodeviewer",
                    "api",
                    "plugin_appkeys",
                    "section_octoprint",
                    "server",
                    "folders",
                    "appearance",
                    "plugin_logging",
                    "plugin_pluginmanager",
                    "plugin_softwareupdate",
                    "plugin_announcements",
                    "plugin_eventmanager",
                    "plugin_backup",
                    "plugin_tracking",
                    "plugin_errortracking",
                    "plugin_pi_support",
                ],
                "usersettings": ["access", "interface"],
                "wizard": [
                    "plugin_softwareupdate_update",
                    "plugin_backup",
                    "plugin_corewizard_acl",
                    "plugin_corewizard_onlinecheck",
                ],
                "about": [
                    "about",
                    "plugin_pi_support",
                    "supporters",
                    "authors",
                    "changelog",
                    "license",
                    "thirdparty",
                    "plugin_pluginmanager",
                ],
                "generic": [],
            },
            "disabled": {
                "navbar": [],
                "sidebar": [],
                "tab": [],
                "settings": [],
                "usersettings": [],
                "generic": [],
            },
        },
    },
    "controls": [],
    "system": {"actions": []},
    "accessControl": {
        "salt": None,
        "userManager": "octoprint.access.users.FilebasedUserManager",
        "groupManager": "octoprint.access.groups.FilebasedGroupManager",
        "permissionManager": "octoprint.access.permissions.PermissionManager",
        "userfile": None,
        "groupfile": None,
        "autologinLocal": False,
        "localNetworks": ["127.0.0.0/8", "::1/128"],
        "autologinAs": None,
        "trustBasicAuthentication": False,
        "checkBasicAuthenticationPassword": True,
        "trustRemoteUser": False,
        "remoteUserHeader": "REMOTE_USER",
        "addRemoteUsers": False,
    },
    "slicing": {"enabled": True, "defaultSlicer": None, "defaultProfiles": None},
    "events": {"enabled": True, "subscriptions": []},
    "api": {"key": None, "allowCrossOrigin": False, "apps": {}},
    "terminalFilters": [
        {
            "name": "Suppress temperature messages",
            "regex": r"(Send: (N\d+\s+)?M105)|(Recv:\s+(ok\s+([PBN]\d+\s+)*)?([BCLPR]|T\d*):-?\d+)",
        },
        {
            "name": "Suppress SD status messages",
            "regex": r"(Send: (N\d+\s+)?M27)|(Recv: SD printing byte)|(Recv: Not SD printing)",
        },
        {
            "name": "Suppress position messages",
            "regex": r"(Send:\s+(N\d+\s+)?M114)|(Recv:\s+(ok\s+)?X:[+-]?([0-9]*[.])?[0-9]+\s+Y:[+-]?([0-9]*[.])?[0-9]+\s+Z:[+-]?([0-9]*[.])?[0-9]+\s+E\d*:[+-]?([0-9]*[.])?[0-9]+).*",
        },
        {"name": "Suppress wait responses", "regex": r"Recv: wait"},
        {
            "name": "Suppress processing responses",
            "regex": r"Recv: (echo:\s*)?busy:\s*processing",
        },
    ],
    "plugins": {"_disabled": [], "_forcedCompatible": []},
    "scripts": {
        "gcode": {
            "afterPrintCancelled": "; disable motors\nM84\n\n;disable all heaters\n{% snippet 'disable_hotends' %}\n{% snippet 'disable_bed' %}\n;disable fan\nM106 S0",
            "snippets": {
                "disable_hotends": "{% if printer_profile.extruder.sharedNozzle %}M104 T0 S0\n{% else %}{% for tool in range(printer_profile.extruder.count) %}M104 T{{ tool }} S0\n{% endfor %}{% endif %}",
                "disable_bed": "{% if printer_profile.heatedBed %}M140 S0\n{% endif %}",
            },
        }
    },
    "estimation": {
        "printTime": {
            "statsWeighingUntil": 0.5,
            "validityRange": 0.15,
            "forceDumbFromPercent": 0.3,
            "forceDumbAfterMin": 30,
            "stableThreshold": 60,
        }
    },
    "devel": {
        "stylesheet": "css",
        "cache": {"enabled": True, "preemptive": True},
        "webassets": {
            "bundle": True,
            "clean_on_startup": True,
            "minify": True,
            "minify_plugins": False,
        },
        "useFrozenDictForPrinterState": True,
        "showLoadingAnimation": True,
        "sockJsConnectTimeout": 30,
        "pluginTimings": False,
    },
}

class PHierarchicalChainMap(PChainMap):
    def deep_dict(self, root=None):
        if root is None:
            root = self

        result = {}
        for key, value in root.items():
            if isinstance(value, dict):
                result[key] = self.deep_dict(root=self.__class__._get_next(key, root))
            else:
                result[key] = value
        return result

    def has_path(self, path, only_local=False, only_defaults=False):
        if only_defaults:
            current = self.parents
        elif only_local:
            current = self.__class__(self.maps[0])
        else:
            current = self

        try:
            for key in path[:-1]:
                value = current[key]
                if isinstance(value, dict):
                    current = self.__class__._get_next(
                        key, current, only_local=only_local
                    )
                else:
                    return False
            return path[-1] in current
        except KeyError:
            return False

    def get_by_path(self, path, only_local=False, only_defaults=False, merged=False):
        if only_defaults:
            current = self.parents
        elif only_local:
            current = self.__class__(self.maps[0])
        else:
            current = self

        for key in path[:-1]:
            value = current[key]
            if isinstance(value, dict):
                current = self.__class__._get_next(key, current, only_local=only_local)
            else:
                raise KeyError(key)

        if merged:
            current = current.deep_dict()
        return current[path[-1]]

    def set_by_path(self, path, value):
        current = self

        for key in path[:-1]:
            if key not in current.maps[0]:
                current.maps[0][key] = {}
            if not isinstance(current[key], dict):
                raise KeyError(key)
            current = self.__class__._hierarchy_for_key(key, current)

        current[path[-1]] = value

    def del_by_path(self, path):
        if not path:
            raise ValueError("Invalid path")

        current = self

        for key in path[:-1]:
            if not isinstance(current[key], dict):
                raise KeyError(key)
            current = self.__class__._hierarchy_for_key(key, current)

        del current[path[-1]]

    @classmethod
    def _hierarchy_for_key(cls, key, chain):
        wrapped_mappings = list()
        for mapping in chain.maps:
            if key in mapping and mapping[key] is not None:
                wrapped_mappings.append(mapping[key])
            else:
                wrapped_mappings.append({})
        return PHierarchicalChainMap(*wrapped_mappings)

    @classmethod
    def _get_next(cls, key, node, only_local=False):
        if isinstance(node, dict):
            return node[key]
        elif only_local and key not in node.maps[0]:
            raise KeyError(key)
        else:
            return cls._hierarchy_for_key(key, node)


def foo(HierarchicalChainMap):
    cm = HierarchicalChainMap({}, default_settings)
    return lambda: cm.deep_dict(None)

print(timeit.timeit(foo(CHierarchicalChainMap), number=1000000))
print(timeit.timeit(foo(PHierarchicalChainMap), number=10000)*100)
