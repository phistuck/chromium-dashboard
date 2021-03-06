# TODO(ericbidelman): generate this file from

# http://src.chromium.org/viewvc/blink/trunk/Source/core/frame/UseCounter.cpp
CSS_PROPERTY_BUCKETS = {
  # 1 was reserved for number of CSS Pages Visited
  2: 'color',
  3: 'direction',
  4: 'display',
  5: 'font',
  6: 'font-family',
  7: 'font-size',
  8: 'font-style',
  9: 'font-variant',
  10: 'font-weight',
  11: 'text-rendering',
  12: 'webkit-font-feature-settings',
  13: 'webkit-font-kerning',
  14: 'webkit-font-smoothing',
  15: 'webkit-font-variant-ligatures',
  16: 'webkit-locale',
  17: 'webkit-text-orientation',
  18: 'webkit-writing-mode',
  19: 'zoom',
  20: 'line-height',
  21: 'background',
  22: 'background-attachment',
  23: 'background-clip',
  24: 'background-color',
  25: 'background-image',
  26: 'background-origin',
  27: 'background-position',
  28: 'background-position-x',
  29: 'background-position-y',
  30: 'background-repeat',
  31: 'background-repeat-x',
  32: 'background-repeat-y',
  33: 'background-size',
  34: 'border',
  35: 'border-bottom',
  36: 'border-bottom-color',
  37: 'border-bottom-left-radius',
  38: 'border-bottom-right-radius',
  39: 'border-bottom-style',
  40: 'border-bottom-width',
  41: 'border-collapse',
  42: 'border-color',
  43: 'border-image',
  44: 'border-image-outset',
  45: 'border-image-repeat',
  46: 'border-image-slice',
  47: 'border-image-source',
  48: 'border-image-width',
  49: 'border-left',
  50: 'border-left-color',
  51: 'border-left-style',
  52: 'border-left-width',
  53: 'border-radius',
  54: 'border-right',
  55: 'border-right-color',
  56: 'border-right-style',
  57: 'border-right-width',
  58: 'border-spacing',
  59: 'border-style',
  60: 'border-top',
  61: 'border-top-color',
  62: 'border-top-left-radius',
  63: 'border-top-right-radius',
  64: 'border-top-style',
  65: 'border-top-width',
  66: 'border-width',
  67: 'bottom',
  68: 'box-shadow',
  69: 'box-sizing',
  70: 'caption-side',
  71: 'clear',
  72: 'clip',
  73: 'webkit-clip-path',
  74: 'content',
  75: 'counter-increment',
  76: 'counter-reset',
  77: 'cursor',
  78: 'empty-cells',
  79: 'float',
  80: 'font-stretch',
  81: 'height',
  82: 'image-rendering',
  83: 'left',
  84: 'letter-spacing',
  85: 'list-style',
  86: 'list-style-image',
  87: 'list-style-position',
  88: 'list-style-type',
  89: 'margin',
  90: 'margin-bottom',
  91: 'margin-left',
  92: 'margin-right',
  93: 'margin-top',
  94: 'max-height',
  95: 'max-width',
  96: 'min-height',
  97: 'min-width',
  98: 'opacity',
  99: 'orphans',
  100: 'outline',
  101: 'outline-color',
  102: 'outline-offset',
  103: 'outline-style',
  104: 'outline-width',
  105: 'overflow',
  106: 'overflow-wrap',
  107: 'overflow-x',
  108: 'overflow-y',
  109: 'padding',
  110: 'padding-bottom',
  111: 'padding-left',
  112: 'padding-right',
  113: 'padding-top',
  114: 'page',
  115: 'page-break-after',
  116: 'page-break-before',
  117: 'page-break-inside',
  118: 'pointer-events',
  119: 'position',
  120: 'quotes',
  121: 'resize',
  122: 'right',
  123: 'size',
  124: 'src',
  125: 'speak',
  126: 'table-layout',
  127: 'tab-size',
  128: 'text-align',
  129: 'text-decoration',
  130: 'text-indent',
  131: 'text-line-through',
  132: 'text-line-through-color',
  133: 'text-line-through-mode',
  134: 'text-line-through-style',
  135: 'text-line-through-width',
  136: 'text-overflow',
  137: 'text-overline',
  138: 'text-overline-color',
  139: 'text-overline-mode',
  140: 'text-overline-style',
  141: 'text-overline-width',
  142: 'text-shadow',
  143: 'text-transform',
  144: 'text-underline',
  145: 'text-underline-color',
  146: 'text-underline-mode',
  147: 'text-underline-style',
  148: 'text-underline-width',
  149: 'top',
  150: 'transition',
  151: 'transition-delay',
  152: 'transition-duration',
  153: 'transition-property',
  154: 'transition-timing-function',
  155: 'unicode-bidi',
  156: 'unicode-range',
  157: 'vertical-align',
  158: 'visibility',
  159: 'white-space',
  160: 'widows',
  161: 'width',
  162: 'word-break',
  163: 'word-spacing',
  164: 'word-wrap',
  165: 'z-index',
  166: 'webkit-animation',
  167: 'webkit-animation-delay',
  168: 'webkit-animation-direction',
  169: 'webkit-animation-duration',
  170: 'webkit-animation-fill-mode',
  171: 'webkit-animation-iteration-count',
  172: 'webkit-animation-name',
  173: 'webkit-animation-play-state',
  174: 'webkit-animation-timing-function',
  175: 'webkit-appearance',
  176: 'webkit-aspect-ratio',
  177: 'webkit-backface-visibility',
  178: 'webkit-background-clip',
  179: 'webkit-background-composite',
  180: 'webkit-background-origin',
  181: 'webkit-background-size',
  182: 'webkit-border-after',
  183: 'webkit-border-after-color',
  184: 'webkit-border-after-style',
  185: 'webkit-border-after-width',
  186: 'webkit-border-before',
  187: 'webkit-border-before-color',
  188: 'webkit-border-before-style',
  189: 'webkit-border-before-width',
  190: 'webkit-border-end',
  191: 'webkit-border-end-color',
  192: 'webkit-border-end-style',
  193: 'webkit-border-end-width',
  194: 'webkit-border-fit',
  195: 'webkit-border-horizontal-spacing',
  196: 'webkit-border-image',
  197: 'webkit-border-radius',
  198: 'webkit-border-start',
  199: 'webkit-border-start-color',
  200: 'webkit-border-start-style',
  201: 'webkit-border-start-width',
  202: 'webkit-border-vertical-spacing',
  203: 'webkit-box-align',
  204: 'webkit-box-direction',
  205: 'webkit-box-flex',
  206: 'webkit-box-flex-group',
  207: 'webkit-box-lines',
  208: 'webkit-box-ordinal-group',
  209: 'webkit-box-orient',
  210: 'webkit-box-pack',
  211: 'webkit-box-reflect',
  212: 'webkit-box-shadow',
  213: 'webkit-color-correction',
  214: 'webkit-column-axis',
  215: 'webkit-column-break-after',
  216: 'webkit-column-break-before',
  217: 'webkit-column-break-inside',
  218: 'webkit-column-count',
  219: 'webkit-column-gap',
  220: 'webkit-column-progression',
  221: 'webkit-column-rule',
  222: 'webkit-column-rule-color',
  223: 'webkit-column-rule-style',
  224: 'webkit-column-rule-width',
  225: 'webkit-column-span',
  226: 'webkit-column-width',
  227: 'webkit-columns',
  228: 'webkit-box-decoration-break',
  229: 'webkit-filter',
  230: 'webkit-align-content',
  231: 'webkit-align-items',
  232: 'webkit-align-self',
  233: 'webkit-flex',
  234: 'webkit-flex-basis',
  235: 'webkit-flex-direction',
  236: 'webkit-flex-flow',
  237: 'webkit-flex-grow',
  238: 'webkit-flex-shrink',
  239: 'webkit-flex-wrap',
  240: 'webkit-justify-content',
  241: 'webkit-font-size-delta',
  242: 'webkit-grid-columns',
  243: 'webkit-grid-rows',
  244: 'webkit-grid-start',
  245: 'webkit-grid-end',
  246: 'webkit-grid-before',
  247: 'webkit-grid-after',
  248: 'webkit-grid-column',
  249: 'webkit-grid-row',
  250: 'webkit-grid-auto-flow',
  251: 'webkit-highlight',
  252: 'webkit-hyphenate-character',
  253: 'webkit-hyphenate-limit-after',
  254: 'webkit-hyphenate-limit-before',
  255: 'webkit-hyphenate-limit-lines',
  256: 'webkit-hyphens',
  257: 'webkit-line-box-contain',
  258: 'webkit-line-align',
  259: 'webkit-line-break',
  260: 'webkit-line-clamp',
  261: 'webkit-line-grid',
  262: 'webkit-line-snap',
  263: 'webkit-logical-width',
  264: 'webkit-logical-height',
  265: 'webkit-margin-after-collapse',
  266: 'webkit-margin-before-collapse',
  267: 'webkit-margin-bottom-collapse',
  268: 'webkit-margin-top-collapse',
  269: 'webkit-margin-collapse',
  270: 'webkit-margin-after',
  271: 'webkit-margin-before',
  272: 'webkit-margin-end',
  273: 'webkit-margin-start',
  274: 'webkit-marquee',
  275: 'webkit-marquee-direction',
  276: 'webkit-marquee-increment',
  277: 'webkit-marquee-repetition',
  278: 'webkit-marquee-speed',
  279: 'webkit-marquee-style',
  280: 'webkit-mask',
  281: 'webkit-mask-box-image',
  282: 'webkit-mask-box-image-outset',
  283: 'webkit-mask-box-image-repeat',
  284: 'webkit-mask-box-image-slice',
  285: 'webkit-mask-box-image-source',
  286: 'webkit-mask-box-image-width',
  287: 'webkit-mask-clip',
  288: 'webkit-mask-composite',
  289: 'webkit-mask-image',
  290: 'webkit-mask-origin',
  291: 'webkit-mask-position',
  292: 'webkit-mask-position-x',
  293: 'webkit-mask-position-y',
  294: 'webkit-mask-repeat',
  295: 'webkit-mask-repeat-x',
  296: 'webkit-mask-repeat-y',
  297: 'webkit-mask-size',
  298: 'webkit-max-logical-width',
  299: 'webkit-max-logical-height',
  300: 'webkit-min-logical-width',
  301: 'webkit-min-logical-height',
  302: 'webkit-nbsp-mode',
  303: 'webkit-order',
  304: 'webkit-padding-after',
  305: 'webkit-padding-before',
  306: 'webkit-padding-end',
  307: 'webkit-padding-start',
  308: 'webkit-perspective',
  309: 'webkit-perspective-origin',
  310: 'webkit-perspective-origin-x',
  311: 'webkit-perspective-origin-y',
  312: 'webkit-print-color-adjust',
  313: 'webkit-rtl-ordering',
  314: 'webkit-ruby-position',
  315: 'webkit-text-combine',
  316: 'webkit-text-decorations-in-effect',
  317: 'webkit-text-emphasis',
  318: 'webkit-text-emphasis-color',
  319: 'webkit-text-emphasis-position',
  320: 'webkit-text-emphasis-style',
  321: 'webkit-text-fill-color',
  322: 'webkit-text-security',
  323: 'webkit-text-stroke',
  324: 'webkit-text-stroke-color',
  325: 'webkit-text-stroke-width',
  326: 'webkit-transform',
  327: 'webkit-transform-origin',
  328: 'webkit-transform-origin-x',
  329: 'webkit-transform-origin-y',
  330: 'webkit-transform-origin-z',
  331: 'webkit-transform-style',
  332: 'webkit-transition',
  333: 'webkit-transition-delay',
  334: 'webkit-transition-duration',
  335: 'webkit-transition-property',
  336: 'webkit-transition-timing-function',
  337: 'webkit-user-drag',
  338: 'webkit-user-modify',
  339: 'webkit-user-select',
  340: 'webkit-flow-into',
  341: 'webkit-flow-from',
  342: 'webkit-region-overflow',
  343: 'webkit-region-break-after',
  344: 'webkit-region-break-before',
  345: 'webkit-region-break-inside',
  346: 'webkit-shape-inside',
  347: 'webkit-shape-outside',
  348: 'webkit-shape-margin',
  349: 'webkit-shape-padding',
  350: 'webkit-wrap-flow',
  351: 'webkit-wrap-through',
  352: 'webkit-wrap',
  353: 'webkit-tap-highlight-color',
  354: 'webkit-app-region',
  355: 'clip-path',
  356: 'clip-rule',
  357: 'mask',
  358: 'enable-background',
  359: 'filter',
  360: 'flood-color',
  361: 'flood-opacity',
  362: 'lighting-color',
  363: 'stop-color',
  364: 'stop-opacity',
  365: 'color-interpolation',
  366: 'color-interpolation-filters',
  367: 'color-profile',
  368: 'color-rendering',
  369: 'fill',
  370: 'fill-opacity',
  371: 'fill-rule',
  372: 'marker',
  373: 'marker-end',
  374: 'marker-mid',
  375: 'marker-start',
  376: 'mask-type',
  377: 'shape-rendering',
  378: 'stroke',
  379: 'stroke-dasharray',
  380: 'stroke-dashoffset',
  381: 'stroke-linecap',
  382: 'stroke-linejoin',
  383: 'stroke-miterlimit',
  384: 'stroke-opacity',
  385: 'stroke-width',
  386: 'alignment-baseline',
  387: 'baseline-shift',
  388: 'dominant-baseline',
  389: 'glyph-orientation-horizontal',
  390: 'glyph-orientation-vertical',
  391: 'kerning',
  392: 'text-anchor',
  393: 'vector-effect',
  394: 'writing-mode',
  395: 'webkit-svg-shadow',
  396: 'webkit-cursor-visibility',
  397: 'image-orientation',
  398: 'image-resolution',
  399: 'webkit-blend-mode',
  400: 'webkit-background-blend-mode',
  401: 'webkit-text-decoration-line',
  402: 'webkit-text-decoration-style',
  403: 'webkit-text-decoration-color',
  404: 'webkit-text-align-last',
  405: 'webkit-text-underline-position',
  406: 'max-zoom',
  407: 'min-zoom',
  408: 'orientation',
  409: 'user-zoom',
  410: 'webkit-dashboard-region',
  411: 'webkit-overflow-scrolling',
  412: 'webkit-app-region',
  413: 'webkit-filter',
  414: 'webkit-box-decoration-break',
  415: 'webkit-tap-highlight-color',
  416: 'buffered-rendering',
  417: 'grid-auto-rows',
  418: 'grid-auto-columns',
  419: 'background-blend-mode',
  420: 'mix-blend-mode',
  421: 'touch-action',
  422: 'grid-area',
  423: 'grid-template-areas',
  424: 'animation',
  425: 'animation-delay',
  426: 'animation-direction',
  427: 'animation-duration',
  428: 'animation-fill-mode',
  429: 'animation-iteration-count',
  430: 'animation-name',
  431: 'animation-play-state',
  432: 'animation-timing-function',
  433: 'object-fit',
  434: 'paint-order',
  435: 'mask-source-type',
  436: 'isolation',
  437: 'object-position',
  438: 'internal-callback',
  439: 'shape-image-threshold',
  440: 'column-fill',
  441: 'text-justify',
  442: 'touch-action-delay',
  443: 'justify-self',
  444: 'scroll-behavior',
  445: 'will-change',
  446: 'transform',
  447: 'transform-origin',
  448: 'transform-style',
  449: 'perspective',
  450: 'perspective-origin',
  451: 'backface-visibility',
  452: 'grid-template',
  453: 'grid',
}

PAGE_VISITS_BUCKET_ID = 52 # corresponds to the property below.

# http://src.chromium.org/viewvc/blink/trunk/Source/core/frame/UseCounter.h
FEATUREOBSERVER_BUCKETS = {
  0: 'PageDestruction',
  1: 'LegacyNotifications',
  2: 'MultipartMainResource',
  3: 'PrefixedIndexedDB',
  4: 'WorkerStart',
  5: 'SharedWorkerStart',
  6: 'LegacyWebAudio',
  7: 'WebAudioStart',
  9: 'UnprefixedIndexedDB',
  10: 'OpenWebDatabase',
  12: 'LegacyTextNotifications',
  13: 'UnprefixedRequestAnimationFrame',
  14: 'PrefixedRequestAnimationFrame',
  15: 'ContentSecurityPolicy',
  16: 'ContentSecurityPolicyReportOnly',
  18: 'PrefixedTransitionEndEvent',
  19: 'UnprefixedTransitionEndEvent',
  20: 'PrefixedAndUnprefixedTransitionEndEvent',
  21: 'AutoFocusAttribute',
  23: 'DataListElement',
  24: 'FormAttribute',
  25: 'IncrementalAttribute',
  26: 'InputTypeColor',
  27: 'InputTypeDate',
  28: 'InputTypeDateTime',
  29: 'InputTypeDateTimeFallback',
  30: 'InputTypeDateTimeLocal',
  31: 'InputTypeEmail',
  32: 'InputTypeMonth',
  33: 'InputTypeNumber',
  34: 'InputTypeRange',
  35: 'InputTypeSearch',
  36: 'InputTypeTel',
  37: 'InputTypeTime',
  38: 'InputTypeURL',
  39: 'InputTypeWeek',
  40: 'InputTypeWeekFallback',
  41: 'ListAttribute',
  42: 'MaxAttribute',
  43: 'MinAttribute',
  44: 'PatternAttribute',
  45: 'PlaceholderAttribute',
  46: 'PrecisionAttribute',
  47: 'PrefixedDirectoryAttribute',
  48: 'PrefixedSpeechAttribute',
  49: 'RequiredAttribute',
  50: 'ResultsAttribute',
  51: 'StepAttribute',
  52: 'PageVisits', # counts are divided by this number for actual %
  53: 'HTMLMarqueeElement',
  55: 'Reflection',
  57: 'PrefixedStorageInfo',
  58: 'XFrameOptions',
  59: 'XFrameOptionsSameOrigin',
  60: 'XFrameOptionsSameOriginWithBadAncestorChain',
  61: 'DeprecatedFlexboxWebContent',
  62: 'DeprecatedFlexboxChrome',
  63: 'DeprecatedFlexboxChromeExtension',
  65: 'UnprefixedPerformanceTimeline',
  66: 'PrefixedPerformanceTimeline',
  67: 'UnprefixedUserTiming',
  69: 'WindowEvent',
  70: 'ContentSecurityPolicyWithBaseElement',
  71: 'PrefixedMediaAddKey',
  72: 'PrefixedMediaGenerateKeyRequest',
  74: 'DocumentClear',
  76: 'SVGFontElement',
  77: 'XMLDocument',
  78: 'XSLProcessingInstruction',
  79: 'XSLTProcessor',
  80: 'SVGSwitchElement',
  82: 'HTMLShadowElementOlderShadowRoot',
  83: 'DocumentAll',
  84: 'FormElement',
  85: 'DemotedFormElement',
  86: 'CaptureAttributeAsEnum',
  87: 'ShadowDOMPrefixedPseudo',
  88: 'ShadowDOMPrefixedCreateShadowRoot',
  89: 'ShadowDOMPrefixedShadowRoot',
  90: 'SVGAnimationElement',
  91: 'KeyboardEventKeyLocation',
  92: 'CaptureEvents',
  93: 'ReleaseEvents',
  94: 'CSSDisplayRunIn',
  95: 'CSSDisplayCompact',
  96: 'LineClamp',
  97: 'SubFrameBeforeUnloadRegistered',
  98: 'SubFrameBeforeUnloadFired',
  99: 'CSSPseudoElementPrefixedDistributed',
  100: 'TextReplaceWholeText',
  101: 'PrefixedShadowRootConstructor',
  102: 'ConsoleMarkTimeline',
  103: 'CSSPseudoElementUserAgentCustomPseudo',
  104: 'DocumentTypeEntities',
  105: 'DocumentTypeInternalSubset',
  106: 'DocumentTypeNotations',
  107: 'ElementGetAttributeNode',
  108: 'ElementSetAttributeNode',
  109: 'ElementRemoveAttributeNode',
  110: 'ElementGetAttributeNodeNS',
  111: 'DocumentCreateAttribute',
  112: 'DocumentCreateAttributeNS',
  113: 'DocumentCreateCDATASection',
  114: 'DocumentInputEncoding',
  115: 'DocumentXMLEncoding',
  116: 'DocumentXMLStandalone',
  117: 'DocumentXMLVersion',
  118: 'NodeIsSameNode',
  119: 'NodeIsSupported',
  120: 'NodeNamespaceURI',
  122: 'NodeLocalName',
  123: 'NavigatorProductSub',
  124: 'NavigatorVendor',
  125: 'NavigatorVendorSub',
  126: 'FileError',
  127: 'DocumentCharset',
  128: 'PrefixedAnimationEndEvent',
  129: 'UnprefixedAnimationEndEvent',
  130: 'PrefixedAndUnprefixedAnimationEndEvent',
  131: 'PrefixedAnimationStartEvent',
  132: 'UnprefixedAnimationStartEvent',
  133: 'PrefixedAndUnprefixedAnimationStartEvent',
  134: 'PrefixedAnimationIterationEvent',
  135: 'UnprefixedAnimationIterationEvent',
  136: 'PrefixedAndUnprefixedAnimationIterationEvent',
  137: 'EventReturnValue',
  138: 'SVGSVGElement',
  139: 'SVGAnimateColorElement',
  140: 'InsertAdjacentText',
  141: 'InsertAdjacentElement',
  142: 'HasAttributes',
  143: 'DOMSubtreeModifiedEvent',
  144: 'DOMNodeInsertedEvent',
  145: 'DOMNodeRemovedEvent',
  146: 'DOMNodeRemovedFromDocumentEvent',
  147: 'DOMNodeInsertedIntoDocumentEvent',
  148: 'DOMCharacterDataModifiedEvent',
  150: 'DocumentAllLegacyCall',
  151: 'HTMLAppletElementLegacyCall',
  152: 'HTMLEmbedElementLegacyCall',
  153: 'HTMLObjectElementLegacyCall',
  154: 'BeforeLoadEvent',
  155: 'GetMatchedCSSRules',
  156: 'SVGFontInCSS',
  157: 'ScrollTopBodyNotQuirksMode',
  158: 'ScrollLeftBodyNotQuirksMode',
  160: 'AttributeOwnerElement',
  162: 'AttributeSpecified',
  163: 'BeforeLoadEventInIsolatedWorld',
  164: 'PrefixedAudioDecodedByteCount',
  165: 'PrefixedVideoDecodedByteCount',
  166: 'PrefixedVideoSupportsFullscreen',
  167: 'PrefixedVideoDisplayingFullscreen',
  168: 'PrefixedVideoEnterFullscreen',
  169: 'PrefixedVideoExitFullscreen',
  170: 'PrefixedVideoEnterFullScreen',
  171: 'PrefixedVideoExitFullScreen',
  172: 'PrefixedVideoDecodedFrameCount',
  173: 'PrefixedVideoDroppedFrameCount',
  176: 'PrefixedElementRequestFullscreen',
  177: 'PrefixedElementRequestFullScreen',
  178: 'BarPropLocationbar',
  179: 'BarPropMenubar',
  180: 'BarPropPersonalbar',
  181: 'BarPropScrollbars',
  182: 'BarPropStatusbar',
  183: 'BarPropToolbar',
  184: 'InputTypeEmailMultiple',
  185: 'InputTypeEmailMaxLength',
  186: 'InputTypeEmailMultipleMaxLength',
  187: 'TextTrackCueConstructor',
  188: 'CSSStyleDeclarationPropertyName',
  189: 'CSSStyleDeclarationFloatPropertyName',
  190: 'InputTypeText',
  191: 'InputTypeTextMaxLength',
  192: 'InputTypePassword',
  193: 'InputTypePasswordMaxLength',
  194: 'SVGInstanceRoot',
  195: 'ShowModalDialog',
  196: 'PrefixedPageVisibility',
  197: 'HTMLFrameElementLocation',
  198: 'CSSStyleSheetInsertRuleOptionalArg',
  199: 'CSSWebkitRegionAtRule',
  200: 'DocumentBeforeUnloadRegistered',
  201: 'DocumentBeforeUnloadFired',
  202: 'DocumentUnloadRegistered',
  203: 'DocumentUnloadFired',
  204: 'SVGLocatableNearestViewportElement',
  205: 'SVGLocatableFarthestViewportElement',
  206: 'IsIndexElement',
  207: 'HTMLHeadElementProfile',
  208: 'OverflowChangedEvent',
  209: 'SVGPointMatrixTransform',
  210: 'HTMLHtmlElementManifest',
  211: 'DOMFocusInOutEvent',
  212: 'FileGetLastModifiedDate',
  213: 'HTMLElementInnerText',
  214: 'HTMLElementOuterText',
  215: 'ReplaceDocumentViaJavaScriptURL',
  216: 'ElementSetAttributeNodeNS',
  217: 'ElementPrefixedMatchesSelector',
  218: 'DOMImplementationCreateCSSStyleSheet',
  219: 'CSSStyleSheetRules',
  220: 'CSSStyleSheetAddRule',
  221: 'CSSStyleSheetRemoveRule',
  222: 'InitMessageEvent',
  223: 'PrefixedInitMessageEvent',
  224: 'ElementSetPrefix',
  225: 'CSSStyleDeclarationGetPropertyCSSValue',
  226: 'SVGElementGetPresentationAttribute',
  229: 'PrefixedMediaCancelKeyRequest',
  230: 'DOMImplementationHasFeature',
  231: 'DOMImplementationHasFeatureReturnFalse',
  232: 'CanPlayTypeKeySystem',
  233: 'PrefixedDevicePixelRatioMediaFeature',
  234: 'PrefixedMaxDevicePixelRatioMediaFeature',
  235: 'PrefixedMinDevicePixelRatioMediaFeature',
  236: 'PrefixedTransform2dMediaFeature',
  237: 'PrefixedTransform3dMediaFeature',
  238: 'PrefixedAnimationMediaFeature',
  239: 'PrefixedViewModeMediaFeature',
  240: 'PrefixedStorageQuota',
  241: 'ContentSecurityPolicyReportOnlyInMeta',
  242: 'PrefixedMediaSourceOpen',
  243: 'ResetReferrerPolicy',
  244: 'CaseInsensitiveAttrSelectorMatch',
  245: 'CaptureAttributeAsBoolean',
  246: 'FormNameAccessForImageElement',
  247: 'FormNameAccessForPastNamesMap',
  248: 'FormAssociationByParser',
  249: 'HTMLSourceElementMedia',
  250: 'SVGSVGElementInDocument',
  251: 'SVGDocumentRootElement',
  252: 'DocumentCreateEventOptionalArgument',
  253: 'MediaErrorEncrypted',
  254: 'EventSourceURL',
  255: 'WebSocketURL',
  256: 'UnsafeEvalBlocksCSSOM',
  257: 'WorkerSubjectToCSP',
  258: 'WorkerAllowedByChildBlockedByScript',
  259: 'HTMLMediaElementControllerNotNull',
  260: 'DeprecatedWebKitGradient',
  261: 'DeprecatedWebKitLinearGradient',
  262: 'DeprecatedWebKitRepeatingLinearGradient',
  263: 'DeprecatedWebKitRadialGradient',
  264: 'DeprecatedWebKitRepeatingRadialGradient',
  265: 'PrefixedGetImageDataHD',
  266: 'PrefixedPutImageDataHD',
  267: 'PrefixedImageSmoothingEnabled',
  268: 'UnprefixedImageSmoothingEnabled',
  269: 'ShadowRootApplyAuthorStyles',
  270: 'PromiseConstructor',
  271: 'PromiseCast',
  272: 'PromiseReject',
  273: 'PromiseResolve',
  274: 'TextAutosizing',
  275: 'TextAutosizingLayout',
  276: 'HTMLAnchorElementPingAttribute',
  277: 'JavascriptExhaustedMemory',
  278: 'InsertAdjacentHTML',
  279: 'SVGClassName',
  280: 'HTMLAppletElement',
  281: 'HTMLMediaElementSeekToFragmentStart',
  282: 'HTMLMediaElementPauseAtFragmentEnd',
  283: 'PrefixedWindowURL',
  284: 'PrefixedWorkerURL',
  285: 'WindowOrientation',
  286: 'DOMStringListContains',
  287: 'DocumentCaptureEvents',
  288: 'DocumentReleaseEvents',
  289: 'WindowCaptureEvents',
  290: 'WindowReleaseEvents',
  291: 'PrefixedGamepad',
  292: 'ElementAnimateKeyframeListEffectObjectTiming',
  293: 'ElementAnimateKeyframeListEffectDoubleTiming',
  294: 'ElementAnimateKeyframeListEffectNoTiming',
  295: 'DocumentXPathCreateExpression',
  296: 'DocumentXPathCreateNSResolver',
  297: 'DocumentXPathEvaluate',
  298: 'AttrGetValue',
  299: 'AttrSetValue',
  300: 'AnimationConstructorKeyframeListEffectObjectTiming',
  301: 'AnimationConstructorKeyframeListEffectDoubleTiming',
  302: 'AnimationConstructorKeyframeListEffectNoTiming',
  303: 'AttrSetValueWithElement',
  304: 'PrefixedCancelAnimationFrame',
  305: 'PrefixedCancelRequestAnimationFrame',
  306: 'NamedNodeMapGetNamedItem',
  307: 'NamedNodeMapSetNamedItem',
  308: 'NamedNodeMapRemoveNamedItem',
  309: 'NamedNodeMapItem',
  310: 'NamedNodeMapGetNamedItemNS',
  311: 'NamedNodeMapSetNamedItemNS',
  312: 'NamedNodeMapRemoveNamedItemNS',
  313: 'OpenWebDatabaseInWorker',
  314: 'OpenWebDatabaseSyncInWorker',
  315: 'PrefixedAllowFullscreenAttribute',
  316: 'XHRProgressEventPosition',
  317: 'XHRProgressEventTotalSize',
  318: 'PrefixedDocumentIsFullscreen',
  319: 'PrefixedDocumentFullScreenKeyboardInputAllowed',
  320: 'PrefixedDocumentCurrentFullScreenElement',
  321: 'PrefixedDocumentCancelFullScreen',
  322: 'PrefixedDocumentFullscreenEnabled',
  323: 'PrefixedDocumentFullscreenElement',
  324: 'PrefixedDocumentExitFullscreen',
  325: 'SVGForeignObjectElement',
  326: 'PrefixedElementRequestPointerLock',
  327: 'SelectionSetPosition',
  328: 'AnimationPlayerFinishEvent',
  329: 'SVGSVGElementInXMLDocument',
  330: 'CanvasRenderingContext2DSetAlpha',
  331: 'CanvasRenderingContext2DSetCompositeOperation',
  332: 'CanvasRenderingContext2DSetLineWidth',
  333: 'CanvasRenderingContext2DSetLineCap',
  334: 'CanvasRenderingContext2DSetLineJoin',
  335: 'CanvasRenderingContext2DSetMiterLimit',
  336: 'CanvasRenderingContext2DClearShadow',
  337: 'CanvasRenderingContext2DSetStrokeColor',
  338: 'CanvasRenderingContext2DSetFillColor',
  339: 'CanvasRenderingContext2DDrawImageFromRect',
  340: 'CanvasRenderingContext2DSetShadow',
  341: 'PrefixedPerformanceClearResourceTimings',
  342: 'PrefixedPerformanceSetResourceTimingBufferSize',
  343: 'EventSrcElement',
  344: 'EventCancelBubble',
  345: 'EventPath',
  346: 'EventClipboardData',
  347: 'NodeIteratorDetach',
  348: 'AttrNodeValue',
  349: 'AttrTextContent',
  350: 'EventGetReturnValueTrue',
  351: 'EventGetReturnValueFalse',
  352: 'EventSetReturnValueTrue',
  353: 'EventSetReturnValueFalse',
  354: 'NodeIteratorExpandEntityReferences',
  355: 'TreeWalkerExpandEntityReferences',
  356: 'WindowOffscreenBuffering',
  357: 'WindowDefaultStatus',
  358: 'WindowDefaultstatus',
  359: 'PrefixedConvertPointFromPageToNode',
  360: 'PrefixedConvertPointFromNodeToPage',
  361: 'PrefixedTransitionEventConstructor',
  362: 'PrefixedMutationObserverConstructor',
  363: 'PrefixedIDBCursorConstructor',
  364: 'PrefixedIDBDatabaseConstructor',
  365: 'PrefixedIDBFactoryConstructor',
  366: 'PrefixedIDBIndexConstructor',
  367: 'PrefixedIDBKeyRangeConstructor',
  368: 'PrefixedIDBObjectStoreConstructor',
  369: 'PrefixedIDBRequestConstructor',
  370: 'PrefixedIDBTransactionConstructor',
  371: 'NotificationPermission',
  372: 'RangeDetach',
  373: 'DocumentImportNodeOptionalArgument',
  374: 'HTMLTableElementVspace',
  375: 'HTMLTableElementHspace',
  376: 'PrefixedDocumentExitPointerLock',
  377: 'PrefixedDocumentPointerLockElement',
  378: 'PrefixedTouchRadiusX',
  379: 'PrefixedTouchRadiusY',
  380: 'PrefixedTouchRotationAngle',
  381: 'PrefixedTouchForce',
  382: 'PrefixedMouseEventMovementX',
  383: 'PrefixedMouseEventMovementY',
  384: 'PrefixedWheelEventDirectionInvertedFromDevice',
  385: 'PrefixedWheelEventInit',
  386: 'PrefixedFileRelativePath',
  387: 'DocumentCaretRangeFromPoint',
  388: 'DocumentGetCSSCanvasContext',
  389: 'ElementScrollIntoViewIfNeeded',
  390: 'ElementScrollByLines',
  391: 'ElementScrollByPages',
  392: 'RangeCompareNode',
  393: 'RangeExpand',
  394: 'HTMLFrameElementWidth',
  395: 'HTMLFrameElementHeight',
  396: 'HTMLImageElementX',
  397: 'HTMLImageElementY',
  398: 'HTMLOptionsCollectionRemoveElement',
  399: 'HTMLPreElementWrap',
  400: 'SelectionBaseNode',
  401: 'SelectionBaseOffset',
  402: 'SelectionExtentNode',
  403: 'SelectionExtentOffset',
  404: 'SelectionType',
  405: 'SelectionModify',
  406: 'SelectionSetBaseAndExtent',
  407: 'SelectionEmpty',
  408: 'SVGFEMorphologyElementSetRadius',
  409: 'VTTCue',
  410: 'VTTCueRender',
  411: 'VTTCueRenderVertical',
  412: 'VTTCueRenderSnapToLinesFalse',
  413: 'VTTCueRenderLineNotAuto',
  414: 'VTTCueRenderPositionNot50',
  415: 'VTTCueRenderSizeNot100',
  416: 'VTTCueRenderAlignNotMiddle',
  417: 'ElementRequestPointerLock',
  418: 'VTTCueRenderRtl',
}
