/*
 Navicat Premium Data Transfer

 Source Server         : local
 Source Server Type    : MySQL
 Source Server Version : 50720
 Source Host           : localhost:3306
 Source Schema         : test

 Target Server Type    : MySQL
 Target Server Version : 50720
 File Encoding         : 65001

 Date: 14/06/2022 20:32:58
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for attack
-- ----------------------------
DROP TABLE IF EXISTS `attack`;
CREATE TABLE `attack`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键，自动增长',
  `source_ip` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '攻击源IP',
  `destination_ip` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '攻击目的IP',
  `attack_type` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '攻击类型',
  `status_of_attack` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '攻击的状态，0表示正在攻击，1表示攻击结束',
  `ground_station_to_attack` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '实施攻击的地面站',
  `ground_station_to_be_attacked` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '被攻击的地面站',
  `time_to_start_attack` datetime(0) NULL DEFAULT NULL COMMENT '开始攻击的时间',
  `time_to_end_attack` datetime(0) NULL DEFAULT NULL COMMENT '结束攻击的时间',
  `last_modified_time` datetime(0) NULL DEFAULT NULL COMMENT '记录修改时间',
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '记录创建时间',
  `delete_status` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '删除状态，0表示未删除，1表示已删除',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
