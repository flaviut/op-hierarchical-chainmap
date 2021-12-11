# Copyright 2021 Gina Häußge & Octoprint contributors
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>
from collections import ChainMap as PyChainMap

example_object = {
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

example_chain = [
    {
        "accessControl": {"salt": "asd"},
        "api": {"key": "fga"},
        "plugins": {
            "HeaterTimeout": {"_config_version": 2, "enabled": True},
            "announcements": {
                "_config_version": 1,
                "channels": {
                    "_blog": {"read_until": 1585659600},
                    "_important": {"read_until": 1521111600},
                    "_octopi": {"read_until": 1573722900},
                    "_plugins": {"read_until": 1585612800},
                    "_releases": {"read_until": 1635874200},
                },
                "enabled_channels": ["_releases", "_important"],
            },
            "arc_welder": {
                "feature_settings": {"file_processing": "manual-only"},
                "notification_settings": {
                    "show_completed_notification": False,
                    "show_progress_bar": False,
                    "show_started_notification": False,
                },
            },
            "bedlevelvisualizer": {"_config_version": 1},
            "detailedprogress": {
                "etl_format": "{hours:02d}h{minutes:02d}m",
                "messages": ["{printTimeLeft} left, ETA {ETA}"],
            },
            "discovery": {"upnpUuid": "d05a7ee7-fc5f-46e2-93ad-46906600e9e4"},
            "errortracking": {"unique_id": "f0e2c5c7-cc3f-4329-b0d9-f6310971981d"},
            "filamentmanager": {
                "_config_version": 1,
                "currencySymbol": "$",
                "database": {"clientID": "fc9c2afa-1890-11ec-a34e-12426f8bc1e6"},
            },
            "firmware_check": {"ignore_infos": True},
            "firmwareupdater": {
                "_config_version": 2,
                "_selected_profile": 0,
                "profiles": [
                    {
                        "_name": "Default",
                        "avrdude_avrmcu": "m1284p",
                        "avrdude_path": "/usr/bin/avrdude",
                        "avrdude_programmer": "arduino",
                        "flash_method": "avrdude",
                        "serial_port": "/dev/ttyUSB0",
                    }
                ],
            },
            "gcodeviewer": {"_config_version": 1},
            "navbartemp": {"displayRaspiTemp": False},
            "softwareupdate": {"_config_version": 9},
            "tracking": {
                "enabled": True,
                "unique_id": "e1eefbd2-3654-4afc-ba68-ed1e58912590",
            },
            "virtual_printer": {"_config_version": 1},
        },
        "printerProfiles": {"default": "_default"},
        "serial": {"autoconnect": True, "baudrate": 250000, "port": "/dev/ttyUSB0"},
        "server": {
            "firstRun": False,
            "incompleteStartup": True,
            "onlineCheck": {"enabled": True},
            "pluginBlacklist": {"enabled": True},
            "secretKey": "aghertgbaetntbea",
            "seenWizards": {"corewizard": 3, "tracking": None},
        },
        "temperature": {
            "profiles": [
                {"bed": 100, "chamber": None, "extruder": 210, "name": "ABS"},
                {"bed": 60, "chamber": None, "extruder": 185, "name": "PLA"},
                {"bed": 80, "chamber": 0, "extruder": 245, "name": "PETG"},
            ]
        },
    },
    {
        "plugins": {
            "action_command_notification": {"enable": True, "enable_popups": False}
        },
        "__overlay__": "hstjjt6",
    },
    {
        "plugins": {
            "softwareupdate": {
                "checks": {
                    "octoprint": {
                        "type": "github_release",
                        "user": "foosel",
                        "repo": "OctoPrint",
                        "method": "pip",
                        "pip": "https://github.com/OctoPrint/OctoPrint/archive/{target_version}.zip",
                        "update_script": '{python} "/opt/octoprint/lib/python3.7/site-packages/octoprint/plugins/softwareupdate/scripts/update-octoprint.py" --branch={branch} --force={force} "{folder}" {target}',
                        "restart": "octoprint",
                        "stable_branch": {
                            "branch": "master",
                            "commitish": ["master"],
                            "name": "Stable",
                        },
                        "prerelease_branches": [
                            {
                                "branch": "rc/maintenance",
                                "commitish": ["rc/maintenance"],
                                "name": "Maintenance RCs",
                            },
                            {
                                "branch": "rc/devel",
                                "commitish": ["rc/maintenance", "rc/devel"],
                                "name": "Devel RCs",
                            },
                        ],
                    }
                },
                "pip_command": None,
                "cache_ttl": 1440,
                "notify_users": True,
                "ignore_throttled": False,
                "minimum_free_storage": 150,
                "check_overlay_url": "https://plugins.octoprint.org/update_check_overlay.json",
                "check_overlay_py2_url": "https://plugins.octoprint.org/update_check_overlay_py2.json",
                "check_overlay_ttl": 360,
                "updatelog_cutoff": 43200,
                "credentials": {
                    "github": None,
                    "bitbucket_user": None,
                    "bitbucket_password": None,
                },
            }
        },
        "__overlay__": "52c0dd10c569fc85ae0c37f5b8f207c5",
    },
    {
        "plugins": {
            "errortracking": {
                "enabled": False,
                "enabled_unreleased": False,
                "unique_id": None,
                "url_server": "https://690e174698034bcc95928e6bfa8573f7@o118517.ingest.sentry.io/1373987",
                "url_coreui": "https://186f1dc5da7d46ab9d6b6de564d839bb@o118517.ingest.sentry.io/1374096",
            }
        },
        "__overlay__": "2683c85fac1ac82a71423522e8166f01",
    },
    {
        "plugins": {
            "pluginmanager": {
                "repository": "https://plugins.octoprint.org/plugins.json",
                "repository_ttl": 1440,
                "notices": "https://plugins.octoprint.org/notices.json",
                "notices_ttl": 360,
                "pip_args": None,
                "pip_force_user": False,
                "confirm_disable": False,
                "dependency_links": False,
                "hidden": [],
                "ignore_throttled": False,
            }
        },
        "__overlay__": "d6e97a54221e1336504889701a8ca8f2",
    },
    {
        "plugins": {
            "announcements": {
                "channels": {
                    "_important": {
                        "name": "Important Announcements",
                        "description": "Important announcements about OctoPrint.",
                        "priority": 1,
                        "type": "rss",
                        "url": "https://octoprint.org/feeds/important.xml",
                    },
                    "_releases": {
                        "name": "Release Announcements",
                        "description": "Announcements of new releases and release candidates of OctoPrint.",
                        "priority": 2,
                        "type": "rss",
                        "url": "https://octoprint.org/feeds/releases.xml",
                    },
                    "_blog": {
                        "name": "On the OctoBlog",
                        "description": "Development news, community spotlights, OctoPrint On Air episodes and more from the official OctoBlog.",
                        "priority": 2,
                        "type": "rss",
                        "url": "https://octoprint.org/feeds/octoblog.xml",
                    },
                    "_plugins": {
                        "name": "New Plugins in the Repository",
                        "description": "Announcements of new plugins released on the official Plugin Repository.",
                        "priority": 2,
                        "type": "rss",
                        "url": "https://plugins.octoprint.org/feed.xml",
                    },
                    "_octopi": {
                        "name": "OctoPi News",
                        "description": "News around OctoPi, the Raspberry Pi image including OctoPrint.",
                        "priority": 2,
                        "type": "rss",
                        "url": "https://octoprint.org/feeds/octopi.xml",
                    },
                },
                "enabled_channels": [
                    "_important",
                    "_releases",
                    "_blog",
                    "_plugins",
                    "_octopi",
                ],
                "forced_channels": ["_important"],
                "channel_order": [
                    "_important",
                    "_releases",
                    "_blog",
                    "_plugins",
                    "_octopi",
                ],
                "ttl": 360,
                "display_limit": 3,
                "summary_limit": 300,
            }
        },
        "__overlay__": "1d7a89d9d320c3a5a17e08280e3a429a",
    },
    {
        "plugins": {
            "discovery": {
                "publicHost": None,
                "publicPort": None,
                "pathPrefix": None,
                "httpUsername": None,
                "httpPassword": None,
                "upnpUuid": None,
                "zeroConf": [],
                "model": {
                    "name": None,
                    "description": None,
                    "number": None,
                    "url": None,
                    "serial": None,
                    "vendor": None,
                    "vendorUrl": None,
                },
                "addresses": None,
                "interfaces": None,
            }
        },
        "__overlay__": "7e767cd814abfdc83fcfd072bbee5189",
    },
    {"plugins": {"corewizard": {}}, "__overlay__": "a60db0c4b810a1a7e8fc8362a05cd0dc"},
    {
        "plugins": {
            "action_command_prompt": {
                "enable": "detected",
                "command": "M876",
                "enable_emergency_sending": True,
                "enable_signal_support": True,
            }
        },
        "__overlay__": "d1f77496b793af4fd846cc918219fbc7",
    },
    {
        "plugins": {
            "gcodeviewer": {
                "mobileSizeThreshold": 2097152,
                "sizeThreshold": 20971520,
                "skipUntilThis": None,
            }
        },
        "__overlay__": "96d72230dff850b8781b95acd9ee8f09",
    },
    {
        "plugins": {
            "tracking": {
                "enabled": None,
                "unique_id": None,
                "server": "https://tracking.octoprint.org/track/{id}/{event}/",
                "ping": 900,
                "pong": 86400,
                "events": {
                    "pong": True,
                    "startup": True,
                    "printjob": True,
                    "commerror": True,
                    "plugin": True,
                    "update": True,
                    "printer": True,
                    "printer_safety_check": True,
                    "throttled": True,
                    "slicing": True,
                    "webui_load": True,
                },
            }
        },
        "__overlay__": "d7daed9ab80d59229207a79c4a56efd8",
    },
    {
        "plugins": {
            "virtual_printer": {
                "enabled": False,
                "okAfterResend": False,
                "forceChecksum": False,
                "numExtruders": 1,
                "pinnedExtruders": None,
                "includeCurrentToolInTemps": True,
                "includeFilenameInOpened": True,
                "hasBed": True,
                "hasChamber": False,
                "repetierStyleTargetTemperature": False,
                "okBeforeCommandOutput": False,
                "smoothieTemperatureReporting": False,
                "klipperTemperatureReporting": False,
                "reprapfwM114": False,
                "sdFiles": {"size": True, "longname": False, "longname_quoted": True},
                "throttle": 0.01,
                "sendWait": True,
                "waitInterval": 1.0,
                "rxBuffer": 64,
                "commandBuffer": 4,
                "supportM112": True,
                "echoOnM117": True,
                "brokenM29": True,
                "brokenResend": False,
                "supportF": False,
                "firmwareName": "Virtual Marlin 1.0",
                "sharedNozzle": False,
                "sendBusy": False,
                "busyInterval": 2.0,
                "simulateReset": True,
                "resetLines": [
                    "start",
                    "Marlin: Virtual Marlin!",
                    "\x80",
                    "SD card ok",
                ],
                "preparedOks": [],
                "okFormatString": "ok",
                "m115FormatString": "FIRMWARE_NAME:{firmware_name} PROTOCOL_VERSION:1.0",
                "m115ReportCapabilities": True,
                "capabilities": {
                    "AUTOREPORT_TEMP": True,
                    "AUTOREPORT_SD_STATUS": True,
                    "AUTOREPORT_POS": False,
                    "EMERGENCY_PARSER": True,
                    "EXTENDED_M20": False,
                },
                "m114FormatString": "X:{x} Y:{y} Z:{z} E:{e[current]} Count: A:{a} B:{b} C:{c}",
                "m105TargetFormatString": "{heater}:{actual:.2f}/ {target:.2f}",
                "m105NoTargetFormatString": "{heater}:{actual:.2f}",
                "ambientTemperature": 21.3,
                "errors": {
                    "checksum_mismatch": "Checksum mismatch",
                    "checksum_missing": "Missing checksum",
                    "lineno_mismatch": "expected line {} got {}",
                    "lineno_missing": "No Line Number with checksum, Last Line: {}",
                    "maxtemp": "MAXTEMP triggered!",
                    "mintemp": "MINTEMP triggered!",
                    "command_unknown": "Unknown command {}",
                },
                "enable_eeprom": True,
                "support_M503": True,
                "resend_ratio": 0,
                "locked": False,
                "passcode": "1234",
            }
        },
        "__overlay__": "3ee2a7dfdeeedfe9f3493d12631edc16",
    },
    {
        "plugins": {"backup": {"restore_unsupported": False}},
        "__overlay__": "2f5ad3b8bd6bff433a31fbd60f7e15e7",
    },
    {
        "plugins": {"eventmanager": {}},
        "__overlay__": "7b1a939b805970e2e867096c4f4c3d72",
    },
    {"plugins": {"logging": {}}, "__overlay__": "a8fc725d58b5c6faf81acdbdd067dbf5"},
    {
        "plugins": {"firmware_check": {"ignore_infos": False}},
        "__overlay__": "2ca68ae55c8d0eb5b7a0582bed60ad06",
    },
    {
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
            "longRunningCommands": [
                "G4",
                "G28",
                "G29",
                "G30",
                "G32",
                "M400",
                "M226",
                "M600",
            ],
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
            "ignoreEmptyPorts": False,
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
            "heartbeat": 900,
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
                "maxSize": 1073741824,
                "nameSuffix": "name",
                "pathSuffix": "path",
            },
            "maxSize": 102400,
            "commands": {
                "systemShutdownCommand": None,
                "systemRestartCommand": None,
                "serverRestartCommand": None,
                "localPipCommand": None,
            },
            "onlineCheck": {
                "enabled": None,
                "interval": 900,
                "host": "1.1.1.1",
                "port": 53,
                "name": "octoprint.org",
            },
            "pluginBlacklist": {
                "enabled": None,
                "url": "https://plugins.octoprint.org/blacklist.json",
                "ttl": 900,
            },
            "diskspace": {"warning": 524288000, "critical": 209715200},
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
            "streamWebrtcIceServers": ["stun:stun.l.google.com:19302"],
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
            "timelapse": {"type": "off", "options": {}, "postRoll": 0, "fps": 25},
            "cleanTmpAfterDays": 7,
            "cacheBuster": False,
        },
        "gcodeAnalysis": {
            "maxExtruders": 10,
            "throttle_normalprio": 0.01,
            "throttle_highprio": 0.0,
            "throttle_lines": 100,
            "runAt": "idle",
            "bedZ": 0.0,
        },
        "feature": {
            "temperatureGraph": True,
            "sdSupport": True,
            "keyboardControl": True,
            "pollWatched": False,
            "modelSizeDetection": True,
            "rememberFileFolder": False,
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
                "regex": "(Send: (N\\d \\s )?M105)|(Recv:\\s (ok\\s ([PBN]\\d \\s )*)?([BCLPR]|T\\d*):-?\\d )",
            },
            {
                "name": "Suppress SD status messages",
                "regex": "(Send: (N\\d \\s )?M27)|(Recv: SD printing byte)|(Recv: Not SD printing)",
            },
            {
                "name": "Suppress position messages",
                "regex": "(Send:\\s (N\\d \\s )?M114)|(Recv:\\s (ok\\s )?X:[ -]?([0-9]*[.])?[0-9] \\s Y:[ -]?([0-9]*[.])?[0-9] \\s Z:[ -]?([0-9]*[.])?[0-9] \\s E\\d*:[ -]?([0-9]*[.])?[0-9] ).*",
            },
            {"name": "Suppress wait responses", "regex": "Recv: wait"},
            {
                "name": "Suppress processing responses",
                "regex": "Recv: (echo:\\s*)?busy:\\s*processing",
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
    },
]


class PyHierarchicalChainMap(PyChainMap):
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
        return PyHierarchicalChainMap(*wrapped_mappings)

    @classmethod
    def _get_next(cls, key, node, only_local=False):
        if isinstance(node, dict):
            return node[key]
        elif only_local and key not in node.maps[0]:
            raise KeyError(key)
        else:
            return cls._hierarchy_for_key(key, node)
