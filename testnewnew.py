from pandas import DataFrame

json1 = [
    {
        "id": "803245389392314371",
        "name": "数字（物理用印：用印次数字段）",
        "fieldLabel": "数字（物理用印：用印次数字段）",
        "fieldType": "NumberComponent",
        "nativeType": "NumberComponent",
        "fieldTags": [
            "WF_MAIN",
            "WF_NUMBER",
            "WF_TEXT",
            "WF_DECIMAL"
        ],
        "detailTableId": "-1",
        "detailDes": "主表字段",
        "required": False,
        "dataSource": "workflow",
        "dataSourceId": "-1",
        "formId": "803245376466337792",
        "complex": False,
        "sFormId": -1,
        "complexId": 0,
        "otherParams": {
            "field_order": 10,
            "otherProperties": "{\"formId\":\"803245376466337792\",\"capitalPosition\":\"outside\",\"isCapital\":False,\"numberType\":\"number\",\"groupId\":\"-1\",\"title\":\"数字（物理用印：用印次数字段）\",\"content\":\"\",\"dataCount\":0,\"dataKey\":\"sz_rbmx3e\",\"pointSize\":\"sel\",\"isDefault\":False,\"isDelimiter\":False,\"name\":\"数字\",\"showOrder\":10.0,\"describe\":\"\",\"placeholder\":\"\",\"componentKey\":\"NumberComponent\",\"fieldId\":\"803245389392314371\"}",
            "dbFieldName": "sz_rbmx3e"
        },
        "delete": False,
        "detail": False
    },
    {
        "id": "803245389392314372",
        "name": "附件（物理用印：用印图片下载字段）",
        "fieldLabel": "附件（物理用印：用印图片下载字段）",
        "fieldType": "FileComponent",
        "nativeType": "FileComponent",
        "fieldTags": [
            "WF_MAIN",
            "WF_ANNEX",
            "WF_FILE_ANNEX"
        ],
        "detailTableId": "-1",
        "detailDes": "主表字段",
        "required": False,
        "dataSource": "workflow",
        "dataSourceId": "-1",
        "formId": "803245376466337792",
        "complex": False,
        "sFormId": -1,
        "complexId": 0,
        "otherParams": {
            "field_order": 11,
            "otherProperties": "{\"formId\":\"803245376466337792\",\"picWidth\":\"0\",\"attmentSizeLimit\":\"3\",\"picHeight\":\"0\",\"groupId\":\"-1\",\"forbinBatchDownload\":False,\"folderSelectType\":\"0\",\"maxNum\":\"0\",\"title\":\"附件（物理用印：用印图片下载字段）\",\"type\":\"File\",\"dataCount\":0,\"dataKey\":\"fj_lrhevy\",\"isDefault\":False,\"isSingle\":False,\"name\":\"附件\",\"files\":[],\"showOrder\":11.0,\"describe\":\"\",\"placeholder\":\"\",\"componentKey\":\"FileComponent\",\"fieldId\":\"803245389392314372\"}",
            "dbFieldName": "fj_lrhevy"
        },
        "delete": False,
        "detail": False
    },
    {
        "id": "803245389392314369",
        "name": "单行文本（物理用印：发起组织字段）",
        "fieldLabel": "单行文本（物理用印：发起组织字段）",
        "fieldType": "Text",
        "nativeType": "Text",
        "fieldTags": [
            "WF_MAIN",
            "WF_TEXT",
            "WF_SINGLE_TEXT"
        ],
        "detailTableId": "-1",
        "detailDes": "主表字段",
        "required": False,
        "dataSource": "workflow",
        "dataSourceId": "-1",
        "formId": "803245376466337792",
        "complex": False,
        "sFormId": -1,
        "complexId": 0,
        "otherParams": {
            "field_order": 8,
            "otherProperties": "{\"formId\":\"803245376466337792\",\"groupId\":\"-1\",\"scan\":False,\"title\":\"单行文本（物理用印：发起组织字段）\",\"content\":\"\",\"dataCount\":0,\"dataKey\":\"dxwb_6p9ktz\",\"isDefault\":False,\"unique\":False,\"name\":\"单行文本\",\"showOrder\":8.0,\"describe\":\"\",\"placeholder\":\"\",\"componentKey\":\"Text\",\"fieldId\":\"803245389392314369\",\"maxLen\":200}",
            "dbFieldName": "dxwb_6p9ktz"
        },
        "delete": False,
        "detail": False
    },
    {
        "id": "803245389392314370",
        "name": "人员选择（物理用印：用印人字段）",
        "fieldLabel": "人员选择（物理用印：用印人字段）",
        "fieldType": "Employee",
        "nativeType": "Employee",
        "fieldTags": [
            "WF_MAIN",
            "WF_BROWSER",
            "WF_HRMRESOURCE",
            "WF_HRMRESOURCE_NEGATIVE"
        ],
        "detailTableId": "-1",
        "detailDes": "主表字段",
        "required": False,
        "dataSource": "workflow",
        "dataSourceId": "-1",
        "formId": "803245376466337792",
        "complex": False,
        "sFormId": -1,
        "complexId": 0,
        "otherParams": {
            "field_order": 9,
            "otherProperties": "{\"formId\":\"803245376466337792\",\"isCurrentEmployee\":False,\"groupId\":\"-1\",\"title\":\"人员选择（物理用印：用印人字段）\",\"dataCount\":0,\"dataKey\":\"ryxz_aegvor\",\"displayType\":\"space\",\"isDefault\":False,\"isSingle\":False,\"name\":\"人员选择\",\"showOrder\":9.0,\"describe\":\"\",\"placeholder\":\"\",\"componentKey\":\"Employee\",\"fieldId\":\"803245389392314370\"}",
            "dbFieldName": "ryxz_aegvor"
        },
        "delete": False,
        "detail": False
    },
    {
        "id": "803245389392314368",
        "name": "单行文本（物理用印：用印主题字段）",
        "fieldLabel": "单行文本（物理用印：用印主题字段）",
        "fieldType": "Text",
        "nativeType": "Text",
        "fieldTags": [
            "WF_MAIN",
            "WF_TEXT",
            "WF_SINGLE_TEXT"
        ],
        "detailTableId": "-1",
        "detailDes": "主表字段",
        "required": False,
        "dataSource": "workflow",
        "dataSourceId": "-1",
        "formId": "803245376466337792",
        "complex": False,
        "sFormId": -1,
        "complexId": 0,
        "otherParams": {
            "field_order": 7,
            "otherProperties": "{\"formId\":\"803245376466337792\",\"groupId\":\"-1\",\"scan\":False,\"title\":\"单行文本（物理用印：用印主题字段）\",\"content\":\"\",\"dataCount\":0,\"dataKey\":\"dxwb_rjuzm2\",\"isDefault\":False,\"unique\":False,\"name\":\"单行文本\",\"showOrder\":7.0,\"describe\":\"\",\"placeholder\":\"\",\"componentKey\":\"Text\",\"fieldId\":\"803245389392314368\",\"maxLen\":200}",
            "dbFieldName": "dxwb_rjuzm2"
        },
        "delete": False,
        "detail": False
    },
    {
        "id": "803245389392314374",
        "name": "单行文本（物理用印：物理印章字段）",
        "fieldLabel": "单行文本（物理用印：物理印章字段）",
        "fieldType": "Text",
        "nativeType": "Text",
        "fieldTags": [
            "WF_MAIN",
            "WF_TEXT",
            "WF_SINGLE_TEXT"
        ],
        "detailTableId": "-1",
        "detailDes": "主表字段",
        "required": False,
        "dataSource": "workflow",
        "dataSourceId": "-1",
        "formId": "803245376466337792",
        "complex": False,
        "sFormId": -1,
        "complexId": 0,
        "otherParams": {
            "field_order": 13,
            "otherProperties": "{\"formId\":\"803245376466337792\",\"groupId\":\"-1\",\"scan\":False,\"title\":\"单行文本（物理用印：物理印章字段）\",\"content\":\"\",\"dataCount\":0,\"dataKey\":\"dxwb_14x920\",\"isDefault\":False,\"unique\":False,\"name\":\"单行文本\",\"showOrder\":13.0,\"describe\":\"\",\"placeholder\":\"\",\"componentKey\":\"Text\",\"fieldId\":\"803245389392314374\",\"maxLen\":200}",
            "dbFieldName": "dxwb_14x920"
        },
        "delete": False,
        "detail": False
    }
]

fieldId_df = DataFrame(json1)
fieldId_df['控件编号'] = fieldId_df.map(lambda x: x["id"])

fieldId = fieldId_df[fieldId_df["name"] == "数字（物理用印：用印次数字段）"]["id"].iloc[0]

# fieldId_df['name'] = fieldId_df['name'].map(lambda x: x["name"])
print(fieldId_df)