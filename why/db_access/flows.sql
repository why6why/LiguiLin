/*
 Navicat Premium Data Transfer

 Source Server         : he.peterli.club
 Source Server Type    : MySQL
 Source Server Version : 80028
 Source Host           : he.peterli.club:9880
 Source Schema         : simulator

 Target Server Type    : MySQL
 Target Server Version : 80028
 File Encoding         : 65001

 Date: 26/06/2022 09:42:22
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for flows
-- ----------------------------
DROP TABLE IF EXISTS `flows`;
CREATE TABLE `flows`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `src_ip` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '源ip',
  `dest_ip` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '目的ip',
  `label` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '预测类别',
  `type_index` int NULL DEFAULT NULL COMMENT '类别下标',
  `attack_frequency` int NULL DEFAULT NULL COMMENT '攻击次数',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2592287 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

SET FOREIGN_KEY_CHECKS = 1;
