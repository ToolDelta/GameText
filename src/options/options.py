options: dict = {
    'options.adjustBrightness=调整亮度，直到您只能看到两个爬行者面部。",
    'options.brightness.notVisible=不可见",
    'options.brightness.barelyVisible=几乎看不见",
    'options.brightness.easilyVisible=清晰可见",
    'options.adUseSingleSignOn=启用单点登录",
    'options.advancedButton=高级视频设置…",
    'options.showAdvancedVideoSettings=显示高级视频设置",
    'options.advancedOpengl=高级 OpenGL",
    'options.advancedVideoTitle=高级视频设置",
    'options.anaglyph=3D效果",
    'options.termsAndConditions=条款和条件",
    'options.attribution=署名",
    'options.3DRendering=3D 渲染",
    'options.animatetextures=动态海浪效果",
    'options.ao=平滑光照",
    'options.ao.max=最大",
    'options.ao.min=最小",
    'options.ao.off=关",
    'options.autojump=自动跳跃",
    'options.sprintOnMovement=冲刺移动",
    'options.clearhotbar=清除热键",
    'options.blockAlternatives=替选方块",
    'options.buildid.format=版本：%1$s",
    'options.protocolversion.format=协议版本：%1%s",
    'options.worldconversion.version=世界转换器：%s",
    'options.builddate.format=创建日期：%s",
    'options.buttonSize=按钮尺寸",
    'options.alwaysHighlightHoveringBoxInCrosshair=突出显示始终打开",
    'options.showActionButton=显示操作按钮",
    'options.enableNewTouchControlSchemes=启用新的触控方案",
    'options.category.addons=附加件",
    'options.category.audio=声音",
    'options.category.classroom_settings=教室",
    'options.category.game=游戏",
    'options.category.graphics=图形",
    'options.category.input=控制",
    'options.category.server=服务器",
    'options.change=更改",
    'options.changeGamertag=更改游戏标签",
    'options.chat.color=颜色",
    'options.chat.height.focused=聚焦高度",
    'options.chat.height.unfocused=淡化高度",
    'options.chat.links=网页链接",
    'options.chat.links.prompt=链接提示",
    'options.chat.opacity=透明度",
    'options.chat.scale=比例",
    'options.chat.title=聊天设置...",
    'options.chat.visibility=聊天",
    'options.chat.visibility.full=显示",
    'options.chat.visibility.hidden=隐藏",
    'options.chat.visibility.system=仅限指令",
    'options.chat.width=宽度",
    'options.codeBuilder=代码编辑器",
    'options.content_log_file=开启内容日志文件",
    'options.content_log_gui=开启内容日志 GUI",
    'options.controller=控制器",
    'options.controllerLayout=控制器布局",
    'options.controllerSettings=控制器设置",
    'options.controls=控制…",
    'options.credits=制作团队",
    'options.crouch=蹲下",
    'options.customizeTitle=自定义世界设置",
    'options.destroyvibration=摧毁方块（震动）",
    'options.debug=调试",
    'options.flighting_debug=飞行调试",
    'options.debugTitle=开发者选项",
    'options.dev_game_tip=游戏提示",
    'options.dev_ad_show_debug_panel=在调试界面中显示教育符号",
    'options.dev_ad_token_refresh_threshold=EDU 登录 Token 刷新阀值秒数",
    'options.dev_playfab_token_refresh_threshold=Playfab 令牌刷新阈值分钟数",
    'options.dev_assertions_debug_break=调试器中的断言中断",
    'options.dev_assertions_show_dialog=断言显示一个模式对话",
    'options.dev_eduDemo=教育演示（需要重新登录）",
    'options.remote_imgui_toggle=已启用远程 Imgui",
    'options.dev_enableDebugUI=启用调试 UI",
    'options.dev_createRealmWithoutPurchase=无购买创建 Realm",
    'options.dev_flushOrphanedRealmsPurchases=清理被遗弃的 Realms 购买",
    'options.dev_enableMixerInteractive=启用 Mixer 交互性命令",
    'options.dev_storeOfferQueryRequiresXbl=需要 XBL 才能享受商店特惠	disable_3rd_party_console_resource_pack_check",
    'options.dev_renderBoundingBox=能见度边界框",
    'options.dev_renderPaths=能见度路径",
    'options.dev_renderGoalState=能见度目标状态",
    'options.dev_renderMobInfoState=渲染生物信息状态",
    'options.dev_resetClientId=重置客户端 ID",
    'options.dev_showChunkMap=显示区块地图",
    'options.dev_chunkMapMode=区块地图查看模式",
    'options.dev_chunk_map_mode_client=客户端",
    'options.dev_chunk_map_mode_server_chunk_state=服务器",
    'options.dev_chunk_map_mode_server_chunk_debug_display_state=服务器（DB 状态）",
    'options.dev_disableRenderTerrain=禁用地形绘制",
    'options.dev_disableRenderEntities=禁用实体绘制",
    'options.dev_disableRenderBlockEntities=禁用方块实体绘制",
    'options.dev_disableRenderParticles=禁用粒子绘制",
    'options.dev_disableRenderSky=禁用天空绘制",
    'options.dev_disableRenderWeather=禁用天气绘制",
    'options.dev_disableRenderHud=禁用 Hud 绘制",
    'options.dev_disableRenderItemInHand=禁用手中物品绘制",
    'options.dev_disableRenderMainMenuCubeMap=禁用主菜单立方体贴图绘制",
    'options.dev_disableRenderMainMenuPaperdollAnimation=禁用主菜单纸娃娃动画",
    'options.dev_serverInstanceThread=服务器实例线程",
    'options.dev_newCuller=使用新的害兽驱除业者",
    'options.dev_showBuildInfo=显示版本信息",
    'options.dev_showDevConsoleButton=显示开发控制台按钮",
    'options.dev_realmsPermissionsEnabledButton=显示 Realm 许可",
    'options.dev_enableProfiler=启用分析器",
    'options.dev_newParticleSystem=启用新粒子系统",
    'options.dev_enableDebugHudOverlay=启用调试 HUD",
    'options.dev_enableDebugHudOverlay.off=关闭",
    'options.dev_enableDebugHudOverlay.basic=基本",
    'options.dev_enableDebugHudOverlay.imgui=ImGui",
    'options.dev_enableDebugHudOverlay.renderchunks=能见度区块",
    'options.dev_enableDebugHudOverlay.workerthreads=工作线程",
    'options.dev_enableDebugHudOverlay.debugtextures=调试纹理",
    'options.dev_enableDebugHudOverlay.profiler=分析器",
    'options.dev_enableDebugHudOverlay.imagememory=图像存储",
    'options.dev_enableDebugHudOverlay.texturememory=材质内存",
    'options.dev_enableDebugHudOverlay.perimagememory=每图像内存",
    'options.dev_enableDebugHudOverlay.buffermemory=缓冲存储器",
    'options.dev_enableDebugHudOverlay.camera=摄像机",
    'options.dev_enableDebugHudOverlay.audio=音频",
    'options.dev_enableDebugHudOverlay.client_network=客户端网络",
    'options.dev_enableDebugHudOverlay.server_network=服务器网络",
    'options.dev_enableDebugHudOverlay.spatial_packet_optimizations=空间数据包优化",
    'options.dev_enableDebugHudOverlay.lock_contention=锁竞争",
    'options.dev_enableDebugHudOverlay.hbui=游戏脸 				 This is a proper name, do not translate",
    'options.dev_transport_layer=传输层类型",
    'options.dev_transport_layer.raknet=RakNet",
    'options.dev_transport_layer.nethernet_xmpp=NetherNet (XMPP)",
    'options.dev_transport_layer.nethernet_mpsd=NetherNet (MPSD)",
    'options.dev_transport_layer.nethernet_websockets=NetherNet (WebSockets)",
    'options.dev_multithreadedRendering=启用多线程渲染",
    'options.dev_file_watcher=开启文件监视器",
    'options.dev_enable_texture_hot_reloader=启用材质热重载器",
    'options.dev_achievementsAlwaysEnabled=成就始终启用",
    'options.dev_useLocalServer=使用本地服务器",
    'options.dev_useIPv6Only=仅使用 IPv6",
    'options.dev_attachPosRenderLevel=渲染连接位置",
    'options.dev_render_attach_pos.none=关闭",
    'options.dev_render_attach_pos.head_pos=头颅位置",
    'options.dev_render_attach_pos.eyes_pos=眼睛位置",
    'options.dev_render_attach_pos.breath_pos=呼吸位置",
    'options.dev_render_attach_pos.body_pos=身体位置",
    'options.dev_render_attach_pos.feet_pos=足部位置",
    'options.dev_render_attach_pos.all=全部",
    'options.dev_disable_client_blob_cache=禁用客户端 Blob 缓存",
    'options.dev_force_client_blob_cache=为本地游戏强制打开客户端 Blob 缓存",
    'options.dev_connectionQuality=连接质量",
    'options.dev_connection_quality.no_limit=无限制",
    'options.dev_connection_quality.phone_4g=4G",
    'options.dev_connection_quality.phone_3g=3G",
    'options.dev_connection_quality.slow=慢",
    'options.dev_connection_quality.very_slow=非常慢",
    'options.dev_use_fps_independent_turning=使用 FPS 独立转弯",
    'options.dev_use_fast_chunk_culling=使用快速区块精选",
    'options.dev_displayMarketplaceDocumentId=显示市场文档 ID",
    'options.dev_addCoins=添加 %s 个硬币",
    'options.discoveryEnvironment=Discovery 环境（需要重新启动）",
    'options.discoveryEnvironment.production=生产",
    'options.discoveryEnvironment.staging=预备",
    'options.discoveryEnvironment.local=本地",
    'options.discoveryEnvironment.dev=开发 [Unstable]",
    'options.dev_realmsEnvironment=Realms 环境",
    'options.dev_realms_environment.production=生产",
    'options.dev_realms_environment.staging=预备",
    'options.dev_realms_environment.local=本地",
    'options.dev_realms_environment.dev=开发",
    'options.dev_realmsSku=Realms SKU",
    'options.dev_realms_sku.production=生产",
    'options.dev_realms_sku.fiveday=五天",
    'options.dev_realms_sku.default=默认",
    'options.dev_realmsEndpoint=Realms 端点",
    'options.dev_realmsEndpointPayment=Realms 端点支付",
    'options.dev_realmsRelyingParty=Realms 信任方",
    'options.dev_realmsRelyingPartyPayment=Realms 信任方支付",
    'options.dev_overrideXboxEnvironmentWindows=覆盖 Xbox 沙盒（在 Windows 上控制的操作系统）",
    'options.dev_overrideXboxEnvironment=覆盖 Xbox 沙盒（需要重新启动）",
    'options.dev_xboxEnvironment=Xbox 沙盒环境（需要重新启动）",
    'options.dev_xbox_environment.retail=零售",
    'options.dev_xbox_environment.dev=开发",
    'options.dev_xbox_environment.dev_achievement=开发成就",
    'options.dev_experimentalTreatment=替代实验处理",
    'options.dev_sandboxRetail=Xforge 沙盒：零售版",
    'options.dev_sandboxDev=Xforge 沙盒：开发版",
    'options.dev_sandboxDevAchievement=Xforge 沙盒：开发成就",
    'options.dev_displayTreatmentsPanel=显示治疗",
    'options.dev_currentTreatmentsTitle=当前治疗",
    'options.dev_unusedTreatmentsTitle=未使用的治疗方法",
    'options.dev_addTreatmentId=添加处理 ID",
    'options.dev_addLabel=添加",
    'options.dev_applyTreatments=应用处理",
    'options.dev_resetToDefault=重置为默认值",
    'options.dev_clearFlights=清除",
    'options.dev_experimentalProgressions=覆盖进程",
    'options.dev_displayProgressionsPanel=显示进程",
    'options.dev_addProgressionId=添加进程 ID",
    'options.dev_reset_day_one_experience=重置第一天游戏内容",
    'options.dev_useZippedInPackagePacks=使用压缩包内的包",
    'options.dev_importPacksAsZip=将包导入为 Zip 压缩包",
    'options.dev_folders_portSettingsFolder=导出设置文件夹",
    'options.dev_useOverrideDate=使用替代日期",
    'options.dev_displayOverrideDatetime=显示日期时间",
    'options.dev_loadOverrideDate=在午餐时加载替代日期时间",
    'options.dev.timeZoneType=替代编辑器时区类型",
    'options.dev.timeZoneType.local=在当地时间下编辑",
    'options.dev.timeZoneType.utc=在 UTC 时间下编辑",
    'options.dev_overrideDateYear=年",
    'options.dev_overrideDateMonth=月",
    'options.dev_overrideDateDay=日",
    'options.dev_overrideDateHour=时",
    'options.dev_overrideDateMinute=分",
    'options.dev_overrideDayLength=替代日长度，以分钟为单位（分钟：1）",
    'options.dev_overrideTimeScale=时间流逝的刻度速度（最小：1，默认：1）",
    'options.dev_updateOverrideDate=更新替代日期",
    'options.dev_overrideVersionMajor=主要",
    'options.dev_overrideVersionMinor=次要",
    'options.dev_overrideVersionPatch=补丁",
    'options.dev_updateVersionOverride=更新客户端版本覆盖",
    'options.dev_resetOverrideDate=重置替代日期时间",
    'options.dev_clearStoreCache=清除市场缓存",
    'options.dev_clearAllCache=清除所有缓存",
    'options.dev_connection_quality=网络调节器（模拟不良连接）",
    'options.dev_connection_off=关闭 - 本地游戏的内存连接已开启",
    'options.dev_connection_nolimit=完整的网络堆栈已开启 - 无限制",
    'options.dev_connection_4g=4G - 15MB 每秒，100 毫秒延迟，1% 的包丢失",
    'options.dev_connection_3g=3G - 1.5MB 每秒，200 毫秒延迟，2% 的包丢失",
    'options.dev_connection_slow=慢 - 400KB 每秒，300 毫秒延迟，3% 的包丢失",
    'options.dev_connection_veryslow=非常慢 - 200KB 每秒，400 毫秒延迟，4% 的包丢失",
    'options.dev_deleteAllPersonas=删除所有角色",
    'options.dev_deleteLegacyPersona=删除历史个性化槽位",
    'options.dev_identity_environment=新的身份和在线基础设施环境（需要重新启动）",
    'options.dev_identity_environment.dev=开发",
    'options.dev_identity_environment.test=测试",
    'options.dev_identity_environment.prod=生产",
    'options.dev_education_services_environment=教育服务（MUTS）环境（需要重新启动）",
    'options.dev_education_environment.dev=开发",
    'options.dev_education_environment.staging=预备",
    'options.dev_education_environment.prod=生产",
    'options.dev_education_environment.local=本地",
    'options.dev.windowsStore=选择 Windows Store（需要重启）",
    'options.dev.windowsStore.auto=自动",
    'options.dev.windowsStore.v6=旧版 Windows Store - V6",
    'options.dev.windowsStore.v8=OneStore - V8",
    'options.dev.stores=当前激活的商店:",
    'options.dev_sunset_overrides=启用日落覆盖",
    'options.dev_sunset_status=将设备视为完全日落",
    'options.dev_sunsetting_tier=夕阳阶段",
    'options.dev_sunsetting_tier.one=阶段 1 - 初始",
    'options.dev_sunsetting_tier.two=阶段 2 - KitKat",
    'options.dev_sunsetting_tier.three=阶段 3 - FireTV",
    'options.dev_sunsetting_tier.four=阶段 4 - TBD",
    'options.dev_sunsetting_tier.not_pending=未搁置",
    'options.difficulty=难度",
    'options.difficulty.easy=简单",
    'options.difficulty.hard=困难",
    'options.difficulty.hardcore=极限",
    'options.difficulty.normal=普通",
    'options.difficulty.peaceful=和平",
    'options.dpadscale=方向键大小",
    'options.enableChatTextToSpeech=聊天文字转语音输出",
    'options.enableAutoPlatformTextToSpeech=设备设置文字转语音输出",
    'options.enableUITextToSpeech=UI 文字转语音输出",
    'options.enableOpenChatMessage=启用开放聊天消息",
    'options.entityShadows=生物的影子",
    'options.editSettings=编辑设置",
    'options.fancyskies=美丽的天空",
    'options.farWarning1=推荐安装64位的Java以使用能见度",
    'options.farWarning2=选项“高” ( 你目前使用的是32位的JAVA )",
    'options.fboEnable=启用帧缓冲器",
    'options.forceUnicodeFont=强制使用Unicode字体",
    'options.fov=视野",
    'options.fov.toggle=FOV 可以通过游戏指南更改",
    'options.licenses=许可",
    'options.licensed_content=授权内容",
    'options.font_license=字体证书",
    'options.font_license_body=%1",
    'options.livingRoomFOV=起居室 FOV",
    'options.default.format=%s",
    'options.percent.format=%s%%",
    'options.fov.format=%s°",
    'options.fov.max=广角",
    'options.fov.min=普通",
    'options.hudOpacity=HUD 不透明度",
    'options.hudOpacity.max=一般",
    'options.hudOpacity.min=隐藏",
    'options.framerateLimit=最大帧率",
    'options.framerateLimit.max=无限制",
    'options.fullKeyboardGameplay=全键盘玩法",
    'options.fullKeyboardLayout=全键盘布局",
    'options.fullscreen=全屏",
    'options.gamepadcursorsensitivity=控制器光标灵敏度",
    'options.gamertag=游戏标签:",
    'options.gamma=亮度",
    'options.gamma.max=明亮",
    'options.gamma.min=昏暗",
    'options.worldLightBrightness=世界光亮度",
    'options.goToFeedbackWebsite=前往反馈网站",
    'options.graphics=精美图像",
    'options.transparentleaves=花俏的树叶",
    'options.bubbleparticles=华丽气泡",
    'options.smooth_lighting=平滑光照",
    'options.upscaling=画质提升",
    'options.raytracing=光线追踪",
    'options.raytracing.disabled.upsell.supported_platform=此选项仅可在游玩支持光线追踪的世界时编辑。请在市场中进行查找，或是制作您自己的支持光线追踪的资源包。",
    'options.raytracing.disabled.upsell.unsupported_platform=您需要特定的设备才能使用此功能，有关更多信息，请参阅：http:",
    'options.graphics.fancy=花俏的",
    'options.graphics.fast=流畅",
    'options.renderingProfile=图形",
    'options.renderingProfile.sad=基本",
    'options.renderingProfile.fancy=花式",
    'options.renderingProfile.superfancy=超级花式",
    'options.group.audio=声音",
    'options.group.feedback=反馈",
    'options.group.game=游戏",
    'options.group.graphics=图形",
    'options.group.graphics.experimental=实验",
    'options.group.input=控制",
    'options.group.multiplayer=多人游戏",
    'options.group.realms=邀请至 Realms Alpha？",
    'options.guiScale=方向键大小",
    'options.guiScale.auto=自动",
    'options.guiScale.large=大",
    'options.guiScale.maximum=最大",
    'options.guiScale.medium=中",
    'options.guiScale.minimum=最小",
    'options.guiScale.normal=普通",
    'options.guiScale.optionName=GUI 标度修正",
    'options.guiScale.small=小",
    'options.hidden=隐藏",
    'options.hidehud=隐藏 HUD",
    'options.hidehand=隐藏手",
    'options.classic_box_selection=轮廓选择",
    'options.creator=创建者",
    'options.creatorTitle=创建者设置",
    'options.vr_classic_box_selection=轮廓选择",
    'options.hidegamepadcursor=隐藏控制器光标",
    'options.hidegui=隐藏GUI",
    'options.hideKeyboardTooltips=隐藏键盘和鼠标提示",
    'options.hidetooltips=隐藏控制器提示",
    'options.splitscreenHUDsize=分屏 HUD 大小",
    'options.ingamePlayerNames=游戏内玩家昵称",
    'options.splitscreenIngamePlayerNames=分屏游戏内玩家昵称",
    'options.interfaceOpacity=HUD 不透明度",
    'options.interactionmodel=交互模型",
    'options.interactionmodel.touch=触摸",
    'options.interactionmodel.crosshair=十字准星",
    'options.interactionmodel.classic=经典",
    'options.splitscreenInterfaceOpacity=分屏 HUD 不透明度",
    'options.textBackgroundOpacity=文本背景透明度",
    'options.hidepaperdoll=隐藏纸娃娃",
    'options.showautosaveicon=显示自动保存图标",
    'options.hold=保留",
    'options.invertMouse=鼠标反转",
    'options.invertYAxis=反转Y轴",
    'options.joystickMoveVisible=移动摇杆可见",
    'options.thumbstickOpacity=摇杆透明度",
    'options.defaultJoystickMoveVisible=不使用时移动摇杆始终可见",
    'options.keyboardLayout=键盘布局",
    'options.keyboardAndMouse=键盘和鼠标",
    'options.keyboardAndMouseSettings=键盘和鼠标设置",
    'options.language=语言",
    'options.languageGuiScaleCompatibility.title=语言和 GUI 比例不兼容",
    'options.languageGuiScaleCompatibility.message.short=如果使用那样小的 GUI 比例，将无法阅读我们为您所选语言套用的字体。",
    'options.languageGuiScaleCompatibility.message.long=如果使用那样小的 GUI 比例，将无法阅读我们为您所选语言套用的字体。您是否要增加 GUI 比例？",
    'options.languageGuiScaleCompatibility.ok=增加 GUI 比例",
    'options.languageGuiScaleCompatibility.cancel=返回",
    'options.languageWarning=译文可能并非100%准确",
    'options.lefthanded=惯用左手者",
    'options.hotbarOnlyTouch=触摸只影响热键",
    'options.manage=管理",
    'options.manageAccount=管理帐户",
    'options.mipmapLevels=Mipmap 级别",
    'options.modelPart.cape=披风",
    'options.modelPart.hat=帽子",
    'options.modelPart.jacket=衣物",
    'options.modelPart.left_pants_leg=左裤腿",
    'options.modelPart.left_sleeve=左袖",
    'options.modelPart.right_pants_leg=右裤腿",
    'options.modelPart.right_sleeve=右袖",
    'options.multiplayer.title=多人游戏设置…",
    'options.music=音乐",
    'options.name=名称",
    'options.defaultName=史蒂夫",
    'options.off=关",
    'options.on=开",
    'options.particles=颗粒效果",
    'options.particles.all=全部",
    'options.particles.decreased=少量",
    'options.particles.minimal=最少",
    'options.patchNotes=补丁说明",
    'options.performanceButton=视频性能设置…",
    'options.performanceVideoTitle=视频性能设置",
    'options.postButton=后期处理设置…",
    'options.postProcessEnable=启用后期处理",
    'options.postVideoTitle=后期处理设置",
    'options.profile=档案",
    'options.profileTitle=用户档案和设置",
    'options.accountError=账户错误",
    'options.accountErrorButton=查看错误",
    'options.qualityButton=视频质量设置…",
    'options.qualityVideoTitle=视频质量设置",
    'options.reducedDebugInfo=简化调试信息",
    'options.renderClouds=云",
    'options.renderDistance=能见度",
    'options.raytracing.renderDistance=光线追踪能见度",
    'options.raytracing.renderDistanceFormat=%s 个区块",
    'options.renderDistanceFormat=%s 个区块",
    'options.renderDistanceRecommendedFormat=%s 个区块（建议）",
    'options.renderDistance.warning=这种高渲染距离可能会导致帧率低、崩溃或其他意外问题的发生",
    'options.raytracing.renderdistance.warning=此设置可能会导致游戏出现性能问题。",
    'options.resetSettings=重置为默认值",
    'options.resetSettings.popUp=是否确实要重置设置？",
    'options.maxFramerate=最大帧率（实验）",
    'options.maxFramerateFormat=%s FPS",
    'options.perf_turtle=性能图表",
    'options.msaa=抗锯齿",
    'options.texelAA=纹素抗锯齿",
    'options.renderDistance.far=高",
    'options.renderDistance.normal=普通",
    'options.renderDistance.short=低",
    'options.renderDistance.tiny=很低",
    'options.resourcepacks=资源包",
    'options.safeZone=安全区",
    'options.safeZoneX=水平安全区",
    'options.safeZoneY=垂直安全区",
    'options.safeZone.title=更改安全区画面",
    'options.safeZone.description=调整滑动条，直到四个角与您的屏幕相适应。",
    'options.saturation=饱和",
    'options.screenAnimations=屏幕动画(重启游戏后生效)",
    'options.screenPositionX=水平屏幕位置",
    'options.screenPositionY=垂直屏幕位置",
    'options.sensitivity=鼠标灵敏度",
    'options.sensitivity.max=超高速！！！",
    'options.sensitivity.min=*哈欠*",
    'options.spyglassdampen=望远镜移动速度",
    'options.staticjoystick=静态摇杆",
    'options.multiplayergame=多人游戏",
    'options.servervisible=对局域网内玩家可见",
    'options.ShowComfortSelectScreen=显示舒适度选择屏幕",
    'options.showInputHints=显示输入提示",
    'options.sliderLabelFormat=%s：%s",
    'options.smoothRotationSpeed=平滑旋转速度",
    'options.xboxliveBroadcast.inviteOnly=仅邀请",
    'options.xboxliveBroadcast.friendsOnly=仅好友",
    'options.xboxliveBroadcast.friendsOfFriends=好友的好友",
    'options.xboxliveBroadcastSettings=Microsoft 账户设置",
    'options.xboxlivevisible=广播到 Xbox 网络用户",
    'options.xboxLiveAccountSettings=Microsoft 账户设置",
    'options.xboxLiveSignedIn=已用 Microsoft 账户登录",
    'options.xboxLiveSignedOut=已从 Microsoft 账户注销",
    'options.xboxLive.privacyControl=隐私和在线安全",
    'options.realms.checkInvites=管理 Realms 成员邀请",
    'options.skinCustomisation=自定义皮肤…",
    'options.skinCustomisation.title=自定义皮肤",
    'options.skin.change=更改皮肤",
    'options.snooper=允许匿名信息反馈",
    'options.snooper.desc=我们意在通过收集你的设备的相关信息，以帮助我们改进《我的世界》。所有的数据都是匿名的，并已经全部列在下方。我们承诺不会用这些数据进行非法行为。但如果你想要取消匿名信息反馈，您随时都可以将其关闭！",
    'options.snooper.title=机器规格集",
    'options.snooper.view=匿名信息反馈设置…",
    'options.sound=音量",
    'options.sounds=音频",
    'options.sounds.title=音频设置",
    'options.accessibility=可访问性",
    'options.accessibility.title=可访问性设置",
    'options.screenShake=摄像机摇晃",
    'options.splitscreen=拆分屏幕",
    'options.splitscreen.horizontal=水平拆分屏幕",
    'options.splitscreen.vertical=垂直拆分屏幕",
    'options.stickyMining=粘性开采",
    'options.stream=直播设置…",
    'options.stream.bytesPerPixel=质量",
    'options.stream.changes=你可能需要重启直播才能使更改生效。",
    'options.stream.chat.enabled=启用",
    'options.stream.chat.enabled.always=总是",
    'options.stream.chat.enabled.never=从不",
    'options.stream.chat.enabled.streaming=直播时",
    'options.stream.chat.title=Twitch聊天设置",
    'options.stream.chat.userFilter=用户过滤器",
    'options.stream.chat.userFilter.all=所有观众",
    'options.stream.chat.userFilter.mods=管理员",
    'options.stream.chat.userFilter.subs=订阅者",
    'options.stream.compression=压缩",
    'options.stream.compression.high=高",
    'options.stream.compression.low=低",
    'options.stream.compression.medium=中",
    'options.stream.estimation=预计分辨率：%dx%d",
    'options.stream.fps=帧率",
    'options.stream.ingest.reset=重置偏好",
    'options.stream.ingest.title=Twitch直播服务器",
    'options.stream.ingestSelection=直播服务器列表",
    'options.stream.kbps=带宽",
    'options.stream.mic_toggle.mute=静音",
    'options.stream.mic_toggle.talk=开启",
    'options.stream.micToggleBehavior=按下来",
    'options.stream.micVolumne=麦克风音量",
    'options.stream.sendMetadata=发送元数据",
    'options.stream.systemVolume=系统音量",
    'options.stream.title=Twitch直播设置",
    'options.thirdperson=摄像机视角",
    'options.thirdperson.firstperson=第一人称",
    'options.thirdperson.thirdpersonback=第三人称背面",
    'options.thirdperson.thirdpersonfront=第三人称正面",
    'options.title=选项",
    'options.toggle=切换",
    'options.renderclouds=渲染云",
    'options.toolboxMode=工具箱模式",
    'options.toggleCrouch=切换蹲下",
    'options.touch=轻触",
    'options.touchSettings=触摸设置",
    'options.touchscreen=触屏模式",
    'options.uiprofile=UI 档案",
    'options.uiprofile.classic=经典",
    'options.uiprofile.pocket=Pocket",
    'options.usetouchpad=分离控制",
    'options.viewSubscriptions=订阅",
    'options.viewSubscriptions.button.info=信息",
    'options.viewSubscriptions.button.price=%s",
    'options.viewSubscriptions.button.pricePerMonth=%s/月",
    'options.viewSubscriptions.button.manage=管理",
    'options.viewSubscriptions.renew=每 30 天续订一次",
    'options.viewSubscriptions.daysRemaining=剩余 %d 天",
    'options.viewSubscriptions.realmsPlus.header=可用订阅",
    'options.viewSubscriptions.realmsPlus.headerAdditional=额外的订阅",
    'options.viewSubscriptions.realmsPlus.detail=超过 150+ 个市场包，及您专属的可容纳 10 名玩家的 Realm 服务器",
    'options.viewSubscriptions.realms.header=额外的订阅",
    'options.viewSubscriptions.realms.detail=可让至多 %d 名玩家同时访问您自己的 Realm 服务器",
    'options.viewSubscriptions.loadingSubscriptions=正在加载您的订阅……",
    'options.viewSubscriptions.loadingSubscriptionsFailed=加载订阅失败",
    'options.viewSubscriptions.purchasedPlatformDiffers=此内容是在 %s 中购买的，您必须使用该设备来管理它。",
    'options.viewSubscriptions.mySubscriptions=我的订阅",
    'options.viewSubscriptions.noActiveSubscriptions=您没有活跃的订阅",
    'options.viewSubscriptions.signIn=登录",
    'options.viewSubscriptions.buyAnAdditionalRealm=购买一个额外的 Realm",
    'options.viewSubscriptions.realmsPlusSubscriptionForRealm=针对 Realm %s 的 Realms Plus 订阅。",
    'options.viewSubscriptions.additionalSubscriptionForRealm=对 Realm %s 的额外订阅",
    'options.viewSubscriptions.personalRealmServer=您专属的 Realm 服务器可以添加无限名好友并且您可以和至多 2 名好友一起在线玩",
    'options.viewSubscriptions.tenPlayers=10 名玩家的 Realm 服务器",
    'options.viewSubscriptions.twoPlayers=2 名玩家的 Realm 服务器",
    'options.viewSubscriptions.startedInStore=始于商店：%s",
    'options.viewSubscriptions.boughtOnAnotherDevice=已在另一台设备上购买",
    'options.viewSubscriptions.deviceSunsetting=您的版本可能很快就会无法访问 Realms",
    'options.viewSubscriptions.deviceSunset=您的版本无法访问 Realms",
    'options.viewSubscriptions.consumableToSubscriptionTransitionInfo=您现在无法扩展您的 Realm。我们现在已经推出了 Realms 的订阅，您可以在您的 Realm 过期后立即购买新的订阅。但是别担心！我们将免费送您 14 天的有效期，您的 Realm 将保持在线，所以您将有足够的时间扩展它。",
    'options.swapJumpAndSneak=交换跳跃和潜行",
    'options.swapGamepadAB=A/B 按钮切换",
    'options.swapGamepadXY=X/Y 按钮切换",
    'options.usetouchscreen=以轻触方式游戏",
    'options.vbo=启用缓冲区顶点对象",
    'options.video=视频",
    'options.videoTitle=视频设置",
    'options.viewBobbing=视角摇晃",
    'options.visible=显示",
    'options.vsync=使用垂直同步",
    'options.vsync.off=无垂直同步",
    'options.vsync.on=垂直同步",
    'options.vsync.adaptive=自适应垂直同步",
    'options.websocketEncryption=需要加密的 Websocket",
    'options.websocketEncryptionWarningLabel=只有当您主动连接到已知且安全的应用程序时才禁用此选项。",
    'options.filelocation.title=文件存储位置",
    'options.filelocation.external=外部",
    'options.filelocation.appdata=应用程序",
    'options.filelocation.external.warning.title=警告",
    'options.filelocation.external.warning.body=外部存储已更改位置，在某些设备上您的世界可能会丢失。请访问以下页面，查看详情：%s",
    'options.filelocation.external.warning.button=详情（启动浏览器）",
    'options.atmosphericsEnable=氛围",
    'options.edgeHighlightEnable=边缘高光",
    'options.bloomEnable=光晕",
    'options.terrainShadowsEnable=地形阴影",
    'options.superFancyWaterEnable=超级花式水",
    'options.onlyTrustedSkinsAllowed=仅允许受信任的皮肤",
    'options.autoUpdateEnabled=自动更新已解锁的包",
    'options.autoUpdateMode=自动更新已解锁的包",
    'options.autoUpdateMode.off=关闭",
    'options.autoUpdateMode.on.withWifiOnly=只在有 Wi-Fi 时打开",
    'options.autoUpdateMode.on.withCellular=在有 Wi-Fi 或者移动数据时打开",
    'options.allowCellularData=使用移动数据",
    'options.cellularDataWarningLabel=使用移动网络进行游戏可能发生额外费用，由运营商收取。",
    'options.turnOffAchievements=关闭成就？",
    'options.turnOffAchievements.message=成就仅对设置为关闭无敌模式的生存模式的世界可用。如果继续，那么即使您在探索前切换回来，也没有人再会在此世界探索时获得成就。",
    'options.achievementsDisabled=本世界中无法获得成就。",
    'options.achievementsDisabled.onLoad=如果您使用这些设置开始游戏，本世界中将不再能够获得成就。",
    'options.achievementsDisabled.notSignedIn=本世界中可以获得成就，但您必须先登录至 Microsoft 账户。",
    'options.turnOffCrossPlatformMultiplayer=关闭跨平台多人游戏？",
    'options.turnOffCrossPlatformMultiplayer.message=您正在尝试使用的内容在跨平台多人课程中禁用。如果继续，您将无法进行跨平台多人课程。",
    'options.conflictingPacks=冲突的包",
    'options.conflictingPacks.message.onStack=已经在堆栈上的包不能和其他包一起使用。 %s",
    'options.conflictingPacks.message.offStack=您正尝试应用的包不能和其他包一起使用。%s",
    'options.conflictingPacks.message.offStackWithBehavior=选择继续会移除所有当前包，然后添加您正尝试应用的包。这将会从世界移除所有行为包，从而使得世界崩溃并使您丢失已创建的内容。",
    'options.conflictingPacks.continue=选择继续会移除所有当前包，然后添加您正尝试应用的包。",
    'options.crossPlatformMultiplayerDisabled=无法在跨平台多人游戏中使用这个世界中活跃的内容。",
    'options.multiplayerDisabled=无法在多人游戏中使用这个世界中活跃的内容。",
    'options.skinsCrossPlatformMultiplayerDisabled=您正在使用的皮肤无法用于跨平台多人游戏。",
    'options.skinsMultiplayerDisabled=您正在使用的皮肤无法用于多人游戏。",
    'options.content.noRealms=编辑世界？",
    'options.content.noRealms.message=这个世界使用了无法在跨平台多人游戏中使用的资源包或模板。",
    'options.experimentalWorldLoad=是否加载实验世界？",
    'options.experimentalWorldLoad.message=这个世界使用的功能仍在开发中。可能随时会出现崩溃、中断或停止工作等问题。",
    'options.updateWorldHeight=世界更新",
    'options.updateWorldHeight.message=此更新可让您的世界变得更高和更深。您当前的世界添加了更多方块和洞穴，所以您拥有了更多可供探索的地下空间。",
    'options.activateExperimentalGameplay.message=小心！您即将在开启实验模式的情况下为您的世界创建一个副本。这个新世界可能会出现未响应、崩溃或无法适应未来推出的更新等问题。",
    'options.activateExperimentalGameplay=激活实验玩法？",
    'options.activateExperimentalGameplay.activate=开启实验",
    'options.activateExperimentalGameplayCreate.message=小心！您正在开启的功能仍在开发中。您的世界可能会出现未响应、崩溃或无法适应未来推出的更新等问题。",
    'options.activateFancyBubbles=激活华丽气泡柱？",
    'options.activateFancyBubblesCreate.message=会启用华丽气泡柱。华丽气泡柱可能会降低一些设备的性能。",
    'options.activateToolboxModeCreate.message=添加用于编辑世界的强大工具。适合使用鼠标和键盘设备、有经验的创建者。",
    'options.activateToolboxModeCreate.messageWithMouse=添加用于编辑世界的强大工具。适合有经验的创建者。",
    'options.unlockTemplateWorldOptions=抛弃创建者的设置？",
    'options.unlockTemplateWorldOptions.message=如果您解锁这些设置，这个模板的创建者希望您拥有的体验可能会被破坏。如果您继续这样做，您可能就无法回到预期的体验。",
    'options.unlockTemplateWorldOptions.initiate=解锁模板世界选项",
    'options.unlockTemplateWorldOptions.ok=解锁所有设置",
    'options.unlockTemplateWorldOptions.cancel=保留创建者设定",
    'options.unlockTemplateWorldOptions.warning=模板世界选项已被锁定在该模板的创建者设置的值上。需要先解锁才能更改。",
    'options.unlockTemplateWorldOptions.packWarning=从游戏设置解锁模板世界选项，以改变这个世界的包。",
    'options.unlockTemplateWorldOptions.permissionsWarning=从游戏设置解锁模板世界选项，以能够更改权限。",
    'options.continue=继续",
    'options.edit=编辑",
    'options.enableEducation=启用 Education Edition？",
    'options.enableEducation.message=会启用 Education Edition 化学功能。教育玩法可能会破坏你的世界。如果您选择继续，我们将以 [EDU] 为开头复制你的世界。",
    'options.enableEducationCreate.message=会启用 Education Edition 化学功能。其在您创建了世界之后将无法关闭。请注意，这些功能在具有中高内存的桌面设备上表现最好。",
    'options.goBack=返回",
    'options.loadWorldAnyway=继续加载世界",
    'options.updateAndPlay=更新和开始",
    'options.makeBackup=制作我的世界的备份副本",
    'options.managePrivacy=若要管理隐私设置，请在任意网络浏览器中访问 https:",
    'options.unlink_msa.button=取消链接 Microsoft 账户",
    'options.unlink_msa.confirm.title=取消链接 Microsoft 账户？",
    'options.unlink_msa.confirm.warning=警告：取消链接后，您将无法在您的账户 %s 上存储您在 'PlayStation 4' 系统上完成的进度或进行的购买。",
    'options.unlink_msa.confirm.warning.2=从此游戏内解除关联您的 Microsoft 账户将影响您在此平台所有使用此 Microsoft 账户的《我的世界》游戏。",
    'options.unlink_msa.confirm.checkbox1=当我在其他平台上玩游戏时，我将不再能够访问任何游戏内商店内容。",
    'options.unlink_msa.confirm.checkbox2=我将不再能够与我的好友在其他平台上玩跨平台游戏。",
    'options.unlink_msa.confirm.checkbox3=我将不再能够访问 Realms，包括当前处于活动状态的 Realms 订阅。",
    'options.unlink_msa.confirm.checkbox4=我理解上述内容，我想继续取消链接。",
    'options.unlink_msa.confirm.button=取消链接",
    'options.unlink_msa.progress.title=正在取消链接",
    'options.unlink_msa.progress.body=正在取消链接您的账户...",
    'options.unlink_msa.success.title=取消链接成功",
    'options.unlink_msa.success.body=您的账户已取消链接。",
    'options.unlink_msa.failure.title=出错了",
    'options.unlink_msa.failure.body=您的账户无法取消链接。是否查看一下您的互联网连接？",
    'options.newUiCreateNewWorld.title=是否想要尝试新 UI？",
    'options.newUiCreateNewWorld.info=§7 还没有完成，但是我们想给您提供一个提前尝试的机会。仅可供特定设备和场景使用。",
    'options.newUiCreateNewWorld.initiate=切换到新 UI",
    'options.newUiCreateNewWorldDialog.title=设置不会保存",
    'options.newUiCreateNewWorldDialog.body=如果返回新设计，那么您将重新开始。确定要继续？",
    'options.newUiCreateNewWorldDialog.accept=前往新设计，不保存",
    'options.newUiCreateNewWorldDialog.stay=留在当前设计",

}